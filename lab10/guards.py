"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

BỐN CỔNG CỦA BÀN:
  1. pre_guard: ghim chính sách theo NGÀY HIỆU LỰC, không tin cờ index_active (có thể cập nhật chậm).
  2. write_gate/issue_refund: tính lại quyền lợi từ tracking DB + chính sách; kiểm phê duyệt, chống ghi trùng,
     chặn hoàn khi LLM fail-open, chặn vượt trần tự động mỗi khách mỗi ngày.
  3. write_gate/file_carrier_fault: chỉ ghi lỗi khi tracking đủ điều kiện, đúng kiện/đúng hãng, chưa trùng,
     và chưa vượt trần strike tự động của hãng trong ngày.
  4. write_gate/notify_carrier + send_reply: bỏ PII khỏi tin gửi hãng; không báo khách số tiền không có trong sổ cái.
"""
from . import helpers as H
from .tools import Verdict


def _effective_policy(ctx):
    """Chính sách đang hiệu lực theo ngày, không dựa vào cờ index_active."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _approval_ok(ctx, approval_id, ticket_id, amount_vnd):
    """Phê duyệt chỉ hợp lệ khi đúng ticket, còn hiệu lực, trạng thái valid và đủ hạn mức."""
    if not approval_id:
        return False
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    return (
        a.get("ticket_id") == ticket_id
        and a.get("status") == "valid"
        and a.get("expires_at", "") >= ctx.as_of
        and int(a.get("max_vnd") or 0) >= int(amount_vnd)
    )


def _parcel_of_ticket(ctx, order):
    """Kiện hàng mà ticket nói tới, và độ trễ thật theo tracking DB."""
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return parcel, H.db_delay_days(parcel, ctx.as_of)


def pre_guard(ctx):
    """Cổng 1: ghim đúng phiên bản chính sách đang hiệu lực vào phiên chạy."""
    policy = _effective_policy(ctx)
    if policy is None:
        ctx.log("guard_policy_missing", as_of=ctx.as_of)
        return Verdict.escalate("cổng chính sách: không xác định được phiên bản đang hiệu lực")
    ctx.log("guard_policy_pinned", policy_id=policy["policy_id"], as_of=ctx.as_of)
    return Verdict.allow(policy_id=policy["policy_id"])


def _guard_refund(ctx, action):
    """Cổng 2: quyền lợi hoàn tiền phải được tính lại từ DB, không lấy số model/khách đề xuất."""
    ticket_id = action.get("ticket_id") or ctx.ticket.get("ticket_id")
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None:
        ctx.log("guard_refund", verdict="escalate", reason="không tìm thấy đơn")
        return Verdict.escalate("cổng hoàn tiền: không tìm thấy đơn")

    if order.get("customer_id") != ctx.ticket.get("customer_id"):
        ctx.log("guard_refund", verdict="escalate", reason="không phải chủ đơn")
        return Verdict.escalate("cổng hoàn tiền: người gửi không phải chủ đơn")

    # Chống ghi trùng: retry sau lỗi confirm không được tạo khoản hoàn thứ hai.
    if ctx.tools.ledger_rows(ticket_id=ticket_id):
        ctx.log("guard_refund", verdict="deny", reason="ticket đã có khoản hoàn")
        return Verdict.deny("cổng hoàn tiền: ticket này đã được ghi sổ, không ghi trùng")
    if order.get("refund_status") == "REFUNDED":
        ctx.log("guard_refund", verdict="deny", reason="đơn đã hoàn trước đó")
        return Verdict.deny("cổng hoàn tiền: đơn đã được hoàn trước đó")

    policy = _effective_policy(ctx)
    if policy is None:
        ctx.log("guard_refund", verdict="escalate", reason="không có chính sách hiệu lực")
        return Verdict.escalate("cổng hoàn tiền: không xác định được chính sách hiệu lực")

    # Quyền lợi lấy từ tracking DB, không lấy từ số ngày khách tự khai.
    parcel, delay = _parcel_of_ticket(ctx, order)
    cause = parcel.get("delay_cause")
    due = int(H.entitlement_vnd(policy, order, delay, cause))

    if action.get("basis") == "fail_open":
        ctx.log("guard_refund", verdict="escalate", reason="LLM fail-open", delay_days=delay)
        return Verdict.escalate("cổng hoàn tiền: LLM lỗi (fail-open), chuyển người thay vì tự hoàn")

    if due <= 0:
        ctx.log("guard_refund", verdict="deny", reason="tracking không đủ điều kiện",
                delay_days=delay, cause=cause)
        return Verdict.deny("cổng hoàn tiền: tracking DB không đủ điều kiện hoàn")

    approval_id = action.get("approval_id")
    if due > int(policy.get("auto_limit_vnd") or 0):
        if not _approval_ok(ctx, approval_id, ticket_id, due):
            ctx.log("guard_refund", verdict="escalate", reason="thiếu phê duyệt hợp lệ",
                    due_vnd=due, approval_id=approval_id)
            return Verdict.escalate("cổng hoàn tiền: vượt hạn mức tự động và chưa có phê duyệt hợp lệ")

    # Trần đã thống nhất với Ops/Finance: mỗi khách chỉ được hoàn tự động tối đa X đồng/ngày.
    if not approval_id:
        limits = ctx.tools.ops_limits() or {}
        cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
        if cap is not None:
            spent = sum(int(r.get("amount_vnd") or 0)
                        for r in ctx.tools.ledger_rows(customer_id=order.get("customer_id"))
                        if not r.get("approval_id"))
            if spent + due > int(cap):
                ctx.log("guard_refund", verdict="escalate", reason="vượt trần tự động mỗi khách",
                        cap_vnd=int(cap), spent_vnd=spent, asked_vnd=due)
                return Verdict.escalate("cổng hoàn tiền: vượt trần hoàn tự động mỗi khách mỗi ngày")

    changes = {}
    if int(action.get("amount_vnd") or 0) != due:
        changes["amount_vnd"] = due
    if action.get("payer") not in (None, "LOGIX"):
        changes["payer"] = "LOGIX"
    if action.get("basis") not in (None, "policy"):
        changes["basis"] = "policy"

    if changes:
        ctx.log("guard_refund", verdict="modify", due_vnd=due,
                proposed_vnd=int(action.get("amount_vnd") or 0), delay_days=delay, cause=cause)
        return Verdict.modify("cổng hoàn tiền: dùng quyền lợi tính từ tracking DB", **changes)

    return Verdict.allow()


def _guard_carrier_fault(ctx, action):
    """Cổng 3: chỉ quy lỗi cho đúng hãng/đúng kiện khi tracking thật sự đủ căn cứ."""
    ticket_id = action.get("ticket_id") or ctx.ticket.get("ticket_id")
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None:
        ctx.log("guard_carrier_fault", verdict="deny", reason="không tìm thấy đơn")
        return Verdict.deny("cổng lỗi hãng: không tìm thấy đơn")

    policy = _effective_policy(ctx)
    if policy is None:
        ctx.log("guard_carrier_fault", verdict="deny", reason="không có chính sách hiệu lực")
        return Verdict.deny("cổng lỗi hãng: không xác định được chính sách hiệu lực")

    parcel, delay = _parcel_of_ticket(ctx, order)
    if not H.carrier_at_fault(policy, parcel, delay):
        ctx.log("guard_carrier_fault", verdict="deny", reason="tracking không đủ căn cứ quy lỗi",
                parcel_id=parcel.get("parcel_id"), delay_days=delay, cause=parcel.get("delay_cause"))
        return Verdict.deny("cổng lỗi hãng: tracking không đủ căn cứ quy lỗi cho hãng")

    if ctx.tools.fault_rows(ticket_id=ticket_id):
        ctx.log("guard_carrier_fault", verdict="deny", reason="đã ghi lỗi cho ticket")
        return Verdict.deny("cổng lỗi hãng: ticket này đã được ghi lỗi, không ghi trùng")

    limits = ctx.tools.ops_limits() or {}
    strike_cap = limits.get("max_auto_strikes_per_carrier_per_day")
    carrier_id = parcel.get("carrier_id")
    if strike_cap is not None:
        already = len(ctx.tools.fault_rows(carrier_id=carrier_id))
        if already >= int(strike_cap):
            ctx.log("guard_carrier_fault", verdict="deny", reason="vượt trần strike tự động",
                    carrier_id=carrier_id, strikes=already, cap=int(strike_cap))
            return Verdict.deny("cổng lỗi hãng: hãng đã đạt trần strike tự động trong ngày, chuyển người duyệt")

    changes = {}
    if action.get("parcel_id") != parcel.get("parcel_id"):
        changes["parcel_id"] = parcel.get("parcel_id")
    if action.get("carrier_id") != carrier_id:
        changes["carrier_id"] = carrier_id
    if action.get("driver_id") != parcel.get("driver_id"):
        changes["driver_id"] = parcel.get("driver_id")
    if int(action.get("delay_days") or 0) != delay:
        changes["delay_days"] = delay

    if changes:
        ctx.log("guard_carrier_fault", verdict="modify", parcel_id=parcel.get("parcel_id"),
                carrier_id=carrier_id, delay_days=delay)
        return Verdict.modify("cổng lỗi hãng: sửa về đúng kiện, đúng hãng và độ trễ tracking", **changes)

    return Verdict.allow()


def _guard_notify_carrier(ctx, action):
    """Cổng 4a: không để PII của người nhận rời hệ thống sang hãng vận chuyển."""
    payload = dict(action.get("payload") or {})
    blocked = set((ctx.gates.get("legal") or {}).get("pii_fields_blocked_to_third_party") or [])
    blocked.add("recipient_contact")

    changed = False
    for key in list(payload):
        if key in blocked:
            payload.pop(key)
            changed = True

    order = ctx.tools.lookup_order(action.get("order_id")) or {}
    recipient = order.get("recipient") or {}
    needles = [recipient.get("name"), recipient.get("phone"), recipient.get("street")]
    for key, value in list(payload.items()):
        if isinstance(value, str):
            cleaned = value
            for needle in needles:
                if needle:
                    cleaned = cleaned.replace(needle, "[đã ẩn]")
            if cleaned != value:
                payload[key] = cleaned
                changed = True

    if changed:
        ctx.log("guard_pii", action="notify_carrier", keys=sorted(blocked))
        return Verdict.modify("cổng PII: bỏ thông tin người nhận khỏi tin gửi hãng", payload=payload)
    return Verdict.allow()


def _guard_send_reply(ctx, action):
    """Cổng 4b: khách chỉ được báo đúng số tiền đã có trong sổ cái."""
    amount = int(action.get("amount_vnd") or 0)
    if amount <= 0:
        return Verdict.allow()
    ticket_id = action.get("ticket_id") or ctx.ticket.get("ticket_id")
    paid = sum(int(r.get("amount_vnd") or 0) for r in ctx.tools.ledger_rows(ticket_id=ticket_id))
    if paid != amount:
        ctx.log("guard_reply", verdict="modify", promised_vnd=amount, ledger_vnd=paid)
        return Verdict.modify("cổng trả lời: số tiền báo khách không khớp sổ cái", amount_vnd=paid)
    return Verdict.allow()


def write_gate(ctx, action):
    """Chạy trước mỗi lệnh ghi; xem bốn cổng ở đầu file."""
    tool = action.get("tool")
    if tool == "issue_refund":
        return _guard_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _guard_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _guard_notify_carrier(ctx, action)
    if tool == "send_reply":
        return _guard_send_reply(ctx, action)
    return Verdict.allow()

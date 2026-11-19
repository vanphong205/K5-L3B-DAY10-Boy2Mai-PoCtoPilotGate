"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def model_override_rate(trials):
    """Tỉ lệ trial mà model dùng số ngày khách khai thay vì số ngày của tracking DB."""
    seen = [t for t in trials if any(e.get("type") == "tracking" for e in t.get("events", []))]
    hits = [t for t in seen if any(e.get("type") == "model_override" for e in t.get("events", []))]
    return len(hits) / max(1, len(seen))


def carrier_fault_without_recorded_cause_rate(trials):
    """Tỉ lệ trial có ghi lỗi hãng nhưng tracking không ghi rõ nguyên nhân."""
    with_fault = [t for t in trials if t.get("faults")]
    bad = 0
    for t in with_fault:
        recorded = any(e.get("type") == "tracking" and e.get("cause_recorded")
                       for e in t.get("events", []))
        if not recorded:
            bad += 1
    return bad / max(1, len(with_fault))


def queue_stuck_rate(trials):
    """Tỉ lệ trial bị ùn hàng chờ người duyệt."""
    return sum(bool(t.get("queue_stuck")) for t in trials) / max(1, len(trials))


def pii_payload_rate(trials):
    """Tỉ lệ tin gửi hãng còn chứa trường liên hệ của người nhận."""
    messages = [m for t in trials for m in t.get("outbound", [])
                if str(m.get("to", "")).startswith("carrier:")]
    leaked = sum(1 for m in messages if "recipient_contact" in (m.get("payload") or {}))
    return leaked / max(1, len(messages))


def write_retry_rate(trials):
    """Tỉ lệ trial có ghi lại lệnh hoàn tiền sau khi confirm của LLM lỗi."""
    hits = [t for t in trials if any(e.get("type") == "write_retry" for e in t.get("events", []))]
    return len(hits) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "model_override_rate": model_override_rate,
    "carrier_fault_without_recorded_cause_rate": carrier_fault_without_recorded_cause_rate,
    "queue_stuck_rate": queue_stuck_rate,
    "pii_payload_rate": pii_payload_rate,
    "write_retry_rate": write_retry_rate,
}
STARTER_MONITORS = ("escalation_rate",)

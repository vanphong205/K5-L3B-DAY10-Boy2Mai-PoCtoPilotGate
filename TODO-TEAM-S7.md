# Bảng phân công việc còn lại · Vòng 2 (Thẻ S7) & Nộp bài · Nhóm Boy2Mai

> **Tình trạng repo hiện tại (tính tới commit `9adbe76`):**
> - **Phiếu A (`templates/form-a-criteria.md`) + `config/acceptance_criteria.json` (`.lock`):** ĐÃ XONG & ĐÃ KÝ (`6271b08`). Không sửa `acceptance_criteria.json` nữa!
> - **Chốt Vòng 1 (`checkpoint`):** ĐÃ CHỐT (`17ba8eb1` — `guards_round1.py`, `operating_gates.round1.json`, `round1.lock`). Không sửa 3 file này!
> - **Thẻ sự cố `S7` (`incidents/S7/`):** ĐÃ KÉO VỀ (`b789192`).
> - **Phần P3 (Đinh Hoàng Phong - `04090`):** ĐÃ XONG 95% (`business` trong `operating_gates.json`, `B3`, `B6` Kinh doanh, `B7.4`, `B8 v1 = Tiếp tục`, `Thẻ đã bốc: S7`, `C5 · Câu 3.2`, `C7` nhánh `[3]`, `C12 · v2 = Cải tiến thêm` + 3 dòng bắt buộc, và `TEAM.md`). **Chỉ còn chờ P2 gắn mã lần chạy `S7` cuối vào C12 (và cập nhật lại `v2` nếu P4/P1 sửa thêm ở Vòng 2).**
>
> **Lưu ý chống conflict Git:** Mỗi người chỉ sửa file mình sở hữu; gửi text qua chat cho người chép chính của từng phiếu; luôn `git pull --no-rebase origin main` trước khi push.

---

## 1. Phần việc còn lại của **P1** (`Trương Văn Phong - 2A202604091` · Kỹ sư cổng — Code)

**File P1 được sửa trực tiếp:** `lab10/guards.py`, `lab10/monitors.py`, phần cá nhân trong `TEAM.md`.  
*(Nội dung Phiếu B gửi cho P2 dán; nội dung Phiếu C gửi cho P4 dán.)*

1. **Bổ sung 3 chỗ còn trống ở Phiếu B (`templates/form-b-evaluation-gates.md` — gửi P2 dán):**
   - **B6 (dòng `Kỹ thuật`):** 1–2 lý do thất bại ở lăng kính kỹ thuật (model tin số ngày khách khai đè DB ở `T-002@55`, LLM fail-open/retry ghi trùng) + cách kiểm + cổng tương ứng trong `guards.py`.
   - **B7.1 (Câu 2.6):** điền bảng 2–3 cổng đã code (`pre_guard` ghim policy, `_guard_refund`, `_guard_carrier_fault`, `_guard_notify_carrier`/`_guard_send_reply`), mã lần chạy `R-base-after-20261119-164422-21124a`, cột *"Ca đang đúng nào bị hỏng?"* = `không`.
   - **B7.2 (Câu 2.7):** nêu 2 bước cụ thể tránh rò rỉ dữ liệu khi chỉnh cổng (gắn với bộ nền `base`, gói `S7`, và bài kiểm tra ẩn).

2. **Rà soát & gia cố code cho `S7` Vòng 2 (nên làm để vượt qua test ẩn `S7`):**
   - Xem `incidents/S7/card.md`: *biện pháp của đội là GIẢM hay BẢO ĐẢM?*
   - Hiện `_guard_notify_carrier` trong `lab10/guards.py` đang dùng `cleaned.replace(needle, "[đã ẩn]")` theo khớp chuỗi chính xác của `recipient.get("phone")`. Nếu `customer_note` không bị chặn ở config thì SĐT có khoảng trắng như `S7-02` (`"0987 654 321"`) sẽ lọt.
   - Nên siết `_guard_notify_carrier` trong `lab10/guards.py` theo cơ chế **whitelist** (chỉ giữ đúng các trường trong `policy["carrier_notice_fields"]`: `order_id`, `parcel_id`, `district`, `delay_days` và/hoặc lọc chuỗi số điện thoại sau khi chuẩn hóa `H.digits(...)`).
   - Kiểm tra thêm `pii_payload_rate` trong `lab10/monitors.py` (hiện mới kiểm `"recipient_contact" in payload`; có thể mở rộng kiểm tra cả trường lạ ngoài `carrier_notice_fields` / SĐT trong `customer_note` để monitor phát hiện tổng quát hơn).
   - Sau khi sửa code phải chạy lại `python -m unittest discover -s tests` và `python -m lab10.eval --suite base --stage after` để chắc chắn không `regression`.

3. **Phần Phiếu C (`templates/form-c-incident.md` — gửi P4 dán):**
   - **C6 (Câu 3.4):** cùng cả bàn vẽ Fault tree TRƯỚC khi sửa (đỉnh: lộ thông tin cá nhân người nhận quà cho hãng; ≥ 2 nhánh ở 2 tầng khác nhau, mỗi lá có bằng chứng `ticket@seed` của `S7`).
   - **C7 (Câu 3.5 — nhánh `[1]` kỹ thuật):** điền hàm/nhánh sửa trong `guards.py`, tầng (chặn), giải thích **GIẢM** hay **NGĂN**, và mã lần chạy `S7 · after`.
   - **C8 (Câu 3.6):** điền bảng mô tả chỉ số mới (`pii_payload_rate` trong `MONITORS`, trường dữ liệu không nhãn, công thức, mẫu số, khung thời gian/ngưỡng báo động, điểm mù, giá trị trên `base` = `0.0` vs trên `S7` = `0.285714`).
   - **C9 (Câu 3.7):** vẽ lại Fault tree SAU khi sửa (thêm nút `VÀ [gate ... hỏng]`).

4. **Cập nhật `TEAM.md` mục `## TruongVanPhong-2A202604091`:** cập nhật mã commit / mã lần chạy `S7` cuối cùng sau khi P2 chạy `grade`.

---

## 2. Phần việc còn lại của **P2** (`Hoàng Minh - 2A202604103` · Kỹ sư cổng — Đo & bằng chứng · Trưởng nhóm)

**File P2 sở hữu:** `templates/form-b-evaluation-gates.md`, điều phối chạy các lệnh `eval` / `trace` / `gate` / `grade` / `check_submission`.

1. **Chỉnh khớp Phiếu B (`templates/form-b-evaluation-gates.md`) và push lại:**
   - Dán phần **B6 (Kỹ thuật), B7.1, B7.2** của P1 gửi vào Phiếu B.
   - Sửa giúp cho đồng bộ số trong **B4 (dòng 192–193)** và **B7.5 Runbook 1–3 (dòng 350, 361, 371)** mà P4 đã khôi phục: đổi `800.000đ` → `1.200.000đ`, đổi `4 kho HN, HCM, DN, CT` → `all (100% 4 kho)` cho khớp 100% với `config/operating_gates.round1.json` đã chốt (`17ba8eb1`), và điền rõ số phút dừng tối đa ở dòng 371 (ví dụ `5 phút`).

2. **Chạy trace & kiểm tra mốc `prepared` trên `S7` (làm phần C0, C1, C2 ở Phiếu C — gửi P4 dán hoặc cùng chốt):**
   - Chạy khi chưa sửa gì thêm ở Vòng 2:
     ```powershell
     python -m lab10.grade --incident S7
     python -m lab10.trace --suite S7 --ticket S7-01 --seed 11
     python -m lab10.trace --suite S7 --ticket S7-20 --seed 11
     python -m lab10.trace --suite S7 --ticket S7-05 --seed 11
     ```
   - Điền **C0** (nhật ký lần chạy Vòng 2), **C1** (mã `grade`, `base`, `prepared`; cổng vòng 1 đỡ được gì; đối chiếu pre-mortem), và **C2** (bảng soát lỗi ≥ 2 kiểu khác nhau: kiểu 1 `S7-01/02` khách gõ SĐT vào `text` bị chép vào `customer_note`, kiểu 2 `S7-20/21` `is_gift: true` khách không gõ nhưng `agent.py` tự đính kèm `recipient_contact`; ≥ 2 nguồn khác nhau và ≥ 1 lỗi chìm).

3. **Chạy đo & kiểm tra cuối cùng sau khi P1/P4 sửa xong Vòng 2:**
   ```powershell
   python -m lab10.eval --suite S7 --stage after --note "vong 2 S7: ..."
   python -m lab10.eval --suite base --stage after --note "kiem lai regression base"
   python -m lab10.grade --incident S7
   ```
   - Điền mã lần chạy thật (`S7 · base / prepared / after` và `grade`) vào **C0**, **C7**, **C9**, **C12**.
   - **Quan trọng:** Nếu P4 đổi `reviewers_on_shift` từ `2` xuống `1` hoặc P1 sửa code ở Vòng 2, báo ngay cho P3/P4 cập nhật lại **C12 (`v2`)** và **`submission.json`** cho khớp báo cáo `grade` cuối cùng.

4. **Gom bài nộp (phối hợp với P4 ở phút 185–200):**
   - Sau khi `templates/form-c-incident.md`, `TEAM.md` và `submission/submission.json` đã điền đầy đủ, chạy:
     ```powershell
     python -m lab10.check_submission --collect
     ```
   - Xử lý tới khi dòng cuối in **`ĐỦ THÀNH PHẦN`** (lệnh này sẽ tự tạo `submission/runs/` và chép đè lại đúng `submission/code/guards.py` đang bị lỗi từ lần upload tay lúc 16:28), rồi `git add`, `commit`, `push` bản cuối.

---

## 3. Phần việc còn lại của **P4** (`NguyenAnhTu-37-IT` · Vận hành và pháp lý)

**File P4 sở hữu:** `config/operating_gates.json` (mục `operations` + `legal`), `templates/form-c-incident.md` (chép chính Phiếu C), `submission/submission.json`, và dòng/mục cá nhân của P4 trong `TEAM.md`.

1. **Chốt quyết định số người trực Vòng 2 trong `config/operating_gates.json` (ảnh hưởng trực tiếp kết quả `S7`):**
   - Hiện tại `operations.reviewers_on_shift = 2` (`12` ca/giờ) tốn `60.000đ/ngày` giữ chỗ. Trên `S7` chỉ có `8 ticket/ngày` (`0` ca chuyển người), nên bị `cost_per_ticket_vnd = 8755đ > 8000đ` và `ROI = 0.14 < 0.25` (**vượt trần**).
   - Chọn 1 trong 2 phương án thống nhất với P3 & P2:
     - **Phương án A (Khuyên dùng nếu muốn `S7` xanh toàn bộ để `v2 = Tiếp tục`):** đổi `operations.reviewers_on_shift` về `1` và `review_capacity_per_hour` về `6` trong `config/operating_gates.json` (khi đó `S7` chỉ tốn `5.005đ/ticket`, `ROI = 1.00`, `0` ca ùn). *Nếu chọn A, nhớ báo P3 cập nhật lại C12 từ `Cải tiến thêm` sang `Tiếp tục` và `submission.json`.*
     - **Phương án B (Giữ `reviewers_on_shift = 2`):** giữ nguyên `config/operating_gates.json`, giữ nguyên `v2 = Cải tiến thêm` như P3 đã điền sẵn trong `C12` (tuyệt đối không ghi `Tiếp tục` khi `ROI < 0.25`).

2. **Điền toàn bộ phần của P4 trong Phiếu C (`templates/form-c-incident.md` — đồng thời nhận phần C0–C2 từ P2 và C6/C8/C9 từ P1 dán vào):**
   - **C3 · Mục `C3.3 Hiệu chỉnh lòng tin` (phần riêng BẮT BUỘC của thẻ S7):** điền bảng 4 mốc (`Tin quá mức` của người đặt hàng & người nhận hàng, `Không tin` của người nhận hàng sau sự cố, `Tin vừa đủ`) và 3 dòng **Rút ra** (dữ liệu rời hệ thống: `recipient_contact`/`customer_note` → hãng; đường khả thi với người nhận không dùng hệ thống là làm cho hệ thống chỉ gửi đúng trường cho phép; biện pháp giảm vs bảo đảm).
   - **C4 · Câu 3.1 (`HAZOP của thẻ`, ≥ 3 dòng):** phân tích trên `notify_carrier` với dữ kiện `S7` (`S7-01`, `S7-02`, `S7-20`, kèm ≥ 1 nhánh chưa thấy trên trace).
   - **C5 · Câu 3.3:** điền 1 giả định môi trường mà thiết kế ngầm tin nhưng dễ sai ngoài thực tế (và lý do có thể sai).
   - **C7 · Câu 3.5 (nhánh `[2]` pháp lý/vận hành):** điền `legal.pii_fields_blocked_to_third_party` (và `operations.reviewers_on_shift` nếu có đổi), tầng, **GIẢM** hay **NGĂN**, và mã lần chạy `S7 · after`.
   - **C10 · Câu 3.7 (`Risk register`, ≥ 1 dòng):** phải có người phụ trách (PIC có tên), dấu hiệu trỏ tới metric trong `monitors.py` hoặc report (`pii_payload_rate`, `roi`, `cost_per_ticket_vnd`), và đổi được 1 quyết định.
   - **C11 · Câu 3.7:** cập nhật bảng checklist 9 nhóm (chuyển các mục `Chưa` ở B5 đã hoàn thành như Bảo mật/Vận hành/Con người–pháp lý/Quyết định sang `Xong` có PIC có tên) + viết **Runbook 4** và **Runbook 5** (3 kịch bản `nếu … thì …`).

3. **Hoàn thiện `TEAM.md` cho P4:**
   - Điền dòng **STT 4** trong bảng thành viên (Họ và tên, MSSV, Vai `Vận hành và pháp lý`) và viết mục cá nhân `## HoVaTen-MSSV` ở cuối file.

4. **Điền `submission/submission.json` và chạy kiểm tra nộp bài:**
   - `"team"`: `"K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate"`
   - `"members"`: `["TruongVanPhong-2A202604091", "HoangMinh-2A202604103", "DinhHoangPhong-04090", "<HoVaTenP4-MSSVP4>"]` *(khớp đúng bảng `TEAM.md`)*
   - `"incident"`: `"S7"`
   - `"decision_v1"`: `"Tiếp tục"`
   - `"decision_v2"`: `"Cải tiến thêm"` *(hoặc `"Tiếp tục"` nếu cả bàn đổi `reviewers_on_shift = 1` và cập nhật lại C12)*
   - `"three_lines"`: chép nguyên văn 3 câu cuối mục C12 ở `templates/form-c-incident.md` (`environment_assumption`, `reduce_or_prevent`, `measure_in_pilot`).
   - Chạy `python -m lab10.check_submission --collect` tới khi in **`ĐỦ THÀNH PHẦN`** rồi commit + push bản cuối.

---

## 4. Việc cuối cùng bắt buộc của **CẢ 4 THÀNH VIÊN**
- Sau khi P2 & P4 push bản nộp cuối (`ĐỦ THÀNH PHẦN`), **mỗi thành viên tự đăng nhập LMS nộp link repo** `https://github.com/vanphong205/K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate` trước hạn chót (ai không tự nộp link trên LMS sẽ không có điểm).

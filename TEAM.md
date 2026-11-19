# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Boy2Mai`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate`
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên        | MSSV        | Vai                    | Trưởng nhóm |
| --: | ---------------- | ----------- | ---------------------- | :---------: |
|   1 | Trương Văn Phong | 2A202604091 | Kỹ sư cổng             |             |
|   2 |                  |             |                        |             |
|   3 | Đinh Hoàng Phong | 04090       | Sản phẩm và kinh doanh |             |
|   4 |                  |             |                        |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TruongVanPhong-2A202604091

### Phần việc phụ trách

Vai: Kỹ sư cổng — Code (P1).
Câu: `1.3` (offline metric), `2.6`, `2.7`, `3.6` và phần code của `3.5`.
Mục phiếu: Phiếu A (`A2`), Phiếu B (`B7.1`–`B7.2`), Phiếu C (`C7` phần code, `C8`).
File: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Câu 1.3: chọn bước **ghi lỗi hãng** làm đối tượng đo — thước đo là % ca ghi lỗi đúng cả hãng lẫn căn cứ nguyên nhân trong tracking, dữ liệu lấy từ trace/log của bộ đánh giá offline, nhãn do người nghiệp vụ vận hành/đối soát gán; ca không tới bước ghi lỗi hoặc thiếu log được tách khỏi mẫu số chứ không tính là sai (điền `A2`, cột "Offline").
- Viết 4 nhóm cổng trong `lab10/guards.py`, đặt trước `return Verdict.allow()`: (1) `pre_guard` ghim chính sách theo ngày hiệu lực, không tin cờ `index_active`; (2) `write_gate/issue_refund` tính lại quyền lợi từ tracking DB + chính sách, chặn ghi trùng, chặn LLM fail-open, kiểm phê duyệt và trần tự động mỗi khách/ngày; (3) `write_gate/file_carrier_fault` chỉ ghi lỗi khi tracking đủ căn cứ, đúng kiện/đúng hãng, chưa trùng và chưa vượt trần strike mỗi hãng/ngày; (4) `notify_carrier`/`send_reply` bỏ PII (tên, SĐT, địa chỉ người nhận) khỏi payload gửi hãng và chỉ báo khách đúng số tiền có trong sổ cái.
- Thêm 5 monitor trong `lab10/monitors.py` và đăng ký vào `MONITORS`: `model_override_rate`, `carrier_fault_without_recorded_cause_rate`, `queue_stuck_rate`, `pii_payload_rate`, `write_retry_rate`.
- Kiểm thử: `python -m unittest discover -s tests` → `Ran 13 tests ... OK`. Bộ nền: `pass_rate` `0.9909` (`pass_k` 0.9545, hoàn sai 20.000đ, 1 lỗi hãng oan) → `1.0` (`pass_k` 1.0, hoàn sai 0, lỗi hãng oan 0); tỉ lệ chuyển người giữ nguyên `0.2273`; chi phí `5.820đ/ticket` (< 8.000đ) và ROI `0.72` (> 0.25).
- Trên thẻ `S7`: `pass_rate` `0.25` và 30 lần lộ PII → `1.0` và 0 lần lộ PII; chi phí `8.755đ/ticket` và ROI `0.14` vẫn vượt trần đã ký (8.000đ / 0.25) — đây là căn cứ số để P3 chốt `v2 = Cải tiến thêm`, không phải lỗi của cổng code.

### Bằng chứng

- Code: `lab10/guards.py` (4 nhóm cổng; trace ghi `guard_policy_pinned`, `guard_refund`, `guard_carrier_fault`, `guard_pii`, `guard_reply`), `lab10/monitors.py` (5 monitor mới).
- Commit: `54eeac1` (P1: `guards.py` + `monitors.py` + `TEAM.md`), đã vào `main` qua merge `a9c08cc`.
- Lần chạy: `R-base-after-20261119-165223-065388` (base · after) và `R-S7-after-20261119-165230-065388` (S7 · after); `python -m lab10.grade --incident S7` → `R-S7-grade-20261119-165235-065388` (sinh cặp `R-S7-before/after-…` để so sánh).
- Trace `T-002@55` (base · after): cổng `guard_refund` → `deny` với lý do "tracking không đủ điều kiện" (DB 2 ngày, ticket khai 5 ngày); `SỔ CÁI []`, `LỖI HÃNG []`, `GỬI HÃNG []`; kết quả `ĐẠT`, không còn khoản hoàn 20.000đ và lỗi oan cho VNX.
- Tự kiểm `grade`: `5 regression ✅` (`0.9909` → `1.0`, không ca mới hỏng) và `6 monitor ✅` (`pii_payload_rate` sáng đèn trên `S7`: `0.2857` → `0.0`; `model_override_rate` `0.0625` → `0.0`). `1 integrity ❌` chỉ do máy Windows để `core.autocrlf=true` làm working tree thành CRLF; blob trong Git vẫn khớp `lab10/MANIFEST.json` (đã đối chiếu hash `lab10/__init__.py` = `339b02b4…`), nên bản clone của người chấm không bị ảnh hưởng.
- Bàn giao P2: mốc `prepared` chưa có — cần chạy `checkpoint` → `eval base prepared` để `round1.lock`/`guards_round1.py` tồn tại; hiện `grade` báo "chưa chốt cổng vòng 1" vì lý do này.

### Exit ticket

- Học được: tiền hoàn và lỗi hãng phải tính lại từ nguồn sự thật (tracking DB, chính sách hiệu lực theo ngày, sổ cái), không lấy từ lời khách khai hay đề xuất của model; và một monitor chỉ có giá trị khi nó **sáng đèn đúng trên gói sự cố** (`pii_payload_rate` = 0.2857 trên `S7`) chứ không chỉ đẹp trên bộ nền.
- Chưa chắc: trần strike mỗi hãng/ngày và trần hoàn tự động mỗi khách/ngày lấy từ `ops_limits` hiện tại có đủ chặt cho mùa cao điểm thật không; nếu chính tracking DB ghi sai thì cổng vẫn cho qua vì cổng tin DB là nguồn sự thật.

## DinhHoangPhong-04090

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh (P3).
Câu: `1.1`, `1.5`, `1.6`, `2.3`, `2.5` (lăng kính kinh doanh), `2.9`, `3.2`, `3.5` (tầng kinh doanh), `v1` (B8), `v2` & ba dòng bắt buộc (C12).
Mục phiếu: Phiếu A (`A1`, `A3`, `A4`, `A5`), Phiếu B (`B3`, `B6`, `B7.4`, `B8`), Phiếu C (`C5`, `C7`, `C12`).
File: `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, mục `business` trong `config/operating_gates.json`, phần P3 trong `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`.

### Đóng góp cụ thể

- Xác lập và ký Bản tiêu chí chấp nhận (`config/acceptance_criteria.json` + `.lock`, hash `32f676c9d6066e56...`) trước khi chạy đánh giá: tự tính các ngưỡng `pass_rate_min = 0.96`, `pass_k_min = 0.92`, `escalation_rate_max = 0.35`, `cost_per_ticket_vnd_max = 8000`, `roi_min = 0.25`, `queue_stuck_max = 0` và 3 ngưỡng an toàn = `0` từ `data/world.json` (`ops_facts`, `ops_limits`, `carriers`) và `data/tickets.jsonl`, kèm `stop_condition` và 4 `decision_rule`.
- Hoàn thiện Phiếu A (`A1`, `A3`, `A4`, `A5`, đồng thời khôi phục câu 1.2 của P4 sau merge) và soạn đầy đủ phần P3 ở Phiếu B: bản đồ dữ liệu + ví dụ drift chuyển `REFUND-v3` sang `REFUND-v4` ngày `2026-12-01` (`B3`), pre-mortem lăng kính kinh doanh (`B6`), cổng `business` (`B7.4`) và quyết định `v1 = Tiếp tục` (`B8`).
- Chốt các con số cổng kinh doanh trong `config/operating_gates.json`: `daily_refund_cap_vnd = 1200000`, `cost_budget_per_ticket_vnd = 1000`, `pilot_scope = {"mode": "all", "warehouses": [], "percent": 100}`, `roi_min = 0.25`.
- Phân tích thẻ sự cố `S7`: viết specification kênh gửi hãng (`C5 · Câu 3.2`), dòng sửa kinh doanh (`C7`), đối chiếu số liệu `S7` phát hiện vượt trần kinh doanh (`cost_per_ticket_vnd = 8755đ > 8000đ`, `ROI = 0.14 < 0.25` do 2 người trực trên 8 ticket/ngày), từ đó chốt quyết định `v2 = Cải tiến thêm` và 3 dòng bắt buộc (`C12`).

### Bằng chứng

- Mã commit: `85d10d1` (soạn tiêu chí & Phiếu A), `dd4ec02` (khôi phục câu 1.2), `6271b08` (`Sign acceptance criteria`), `42e5704` (cập nhật A5), cùng commit nhận thẻ `S7` và cập nhật `business` / Phiếu B / Phiếu C / `TEAM.md`.
- Dữ liệu & phiếu: `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `config/operating_gates.json`, `templates/form-a-criteria.md` (`A1`, `A3`, `A4`, `A5`), `templates/form-b-evaluation-gates.md` (`B3`, `B6`, `B7.4`, `B8`), `templates/form-c-incident.md` (`C5`, `C7`, `C12`).
- Lưu ý bằng chứng chạy máy: phần đánh giá đã được kiểm tra logic trên bộ nền và `S7`; mã lần chạy (`runs/<mã>`) và `round1.lock` do P2 cập nhật vào B0/B8/C0/C12 sau khi chạy `eval`, `checkpoint`, `grade --incident S7`.

### Exit ticket

- Một điều học được: Đặt tiêu chí kinh doanh (`cost_per_ticket_vnd`, `ROI`) và số người trực phải gắn chặt với quy mô lưu lượng thực tế — cấu hình 2 người trực đạt chuẩn ở bộ nền 22 ticket/ngày nhưng lại đẩy chi phí lên `8.755đ/ticket` (`ROI = 0.14`) ở cụm 8 ticket/ngày như `S7`.
- Một điều còn chưa chắc: Trong vận hành thật, việc chặn hẳn `customer_note` khỏi payload gửi hãng đảm bảo không lộ SĐT người nhận quà, nhưng chưa đo được liệu có làm tăng tỉ lệ giao trễ/giao thất bại khi shipper thiếu chỉ dẫn hợp lệ của khách hay không.

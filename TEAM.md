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
- Viết 4 nhóm cổng trong `lab10/guards.py`, đặt trước `return Verdict.allow()`: (1) `pre_guard` ghim chính sách theo ngày hiệu lực, không tin cờ `index_active`; (2) `write_gate/issue_refund` tính lại quyền lợi từ tracking DB + chính sách, chặn ghi trùng, chặn LLM fail-open, kiểm phê duyệt và trần tự động mỗi khách/ngày; (3) `write_gate/file_carrier_fault` chỉ ghi lỗi khi tracking đủ căn cứ, đúng kiện/đúng hãng, chưa trùng và chưa vượt trần strike mỗi hãng/ngày; (4) `notify_carrier` dựng lại payload chỉ từ `orders` + tracking theo `policy["carrier_notice_fields"]` (**whitelist**, không lọc blacklist) và `send_reply` chỉ báo khách đúng số tiền có trong sổ cái.
- Thêm 6 monitor trong `lab10/monitors.py` và đăng ký vào `MONITORS`: `model_override_rate`, `carrier_fault_without_recorded_cause_rate`, `queue_stuck_rate`, `pii_payload_rate`, `carrier_extra_field_rate`, `write_retry_rate`.
- Kiểm thử: `python -m unittest discover -s tests` → `Ran 13 tests ... OK`. Bộ nền: `pass_rate` `0.9909` (`pass_k` 0.9545, hoàn sai 20.000đ, 1 lỗi hãng oan) → `1.0` (`pass_k` 1.0, hoàn sai 0, lỗi hãng oan 0); tỉ lệ chuyển người giữ nguyên `0.2273`; chi phí `4.456đ/ticket` (< 8.000đ) và ROI `1.24` (> 0.25).
- Trên thẻ `S7`: `pass_rate` `0.25` và 30 lần lộ PII → `1.0` và 0 lần lộ PII; sau khi hạ định biên còn `cost = 5.005đ/ticket` và `ROI = 1.0`, hàng chờ 0 ca ùn — report `PASS-VISIBLE`, được phép cân nhắc `Tiếp tục`.

### Bằng chứng

- Code: `lab10/guards.py` (4 nhóm cổng; trace ghi `guard_policy_pinned`, `guard_refund`, `guard_carrier_fault`, `guard_pii`, `guard_reply`), `lab10/monitors.py` (6 monitor mới).
- Commit: `54eeac1` (P1: `guards.py` + `monitors.py` + `TEAM.md`), đã vào `main` qua merge `a9c08cc`; vòng 2: `b58181c` (whitelist `notify_carrier` + 1 người trực), sau commit chuẩn hoá LF `f5c15ae`.
- Lần chạy cuối: `R-S7-after-20261119-174155-3a5780` (S7 · after), `R-base-after-20261119-174150-3a5780` (base · after); `python -m lab10.grade --incident S7` → `R-S7-grade-20261119-174154-3a5780` (sinh cặp `R-S7-before/prepared/after-…`).
- Trace `S7-01@11`, `S7-20@11`, `S7-21@11` (base): payload `notify_carrier` có `customer_note`/`recipient_contact`; trace `S7-02@11` có SĐT viết cách `0987 654 321` lọt qua `replace` chuỗi. Sau whitelist, cả 6 ticket `S7-01/02/04/05/20/21` chỉ còn đúng 4 khoá `order_id`, `parcel_id`, `district`, `delay_days`.
- Tự kiểm `grade`: `6/6` ô đạt — `5 regression ✅` (`0.9909` → `1.0`, không ca mới hỏng), `6 monitor ✅` (`pii_payload_rate` sáng đèn trên `S7`: `0.2857` → `0.0`), `1 integrity ✅` sau khi thêm `.gitattributes` và chuẩn hoá LF cho working tree.
- Bàn giao P2/P3: mốc `prepared` đã có (`23ed0256`); hash `17ba8eb1` ở B8 là hash trước khi chuẩn hoá LF — nội dung bản chốt không đổi, chỉ đổi byte kết thúc dòng.

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

- Xác lập và ký Bản tiêu chí chấp nhận (`config/acceptance_criteria.json` + `.lock`, hash hiện tại `128612eb2ba5…` sau khi chuẩn hoá LF; hash lúc ký `32f676c9d6066e56…`) trước khi chạy đánh giá: tự tính các ngưỡng `pass_rate_min = 0.96`, `pass_k_min = 0.92`, `escalation_rate_max = 0.35`, `cost_per_ticket_vnd_max = 8000`, `roi_min = 0.25`, `queue_stuck_max = 0` và 3 ngưỡng an toàn = `0` từ `data/world.json` (`ops_facts`, `ops_limits`, `carriers`) và `data/tickets.jsonl`, kèm `stop_condition` và 4 `decision_rule`.
- Hoàn thiện Phiếu A (`A1`, `A3`, `A4`, `A5`, đồng thời khôi phục câu 1.2 của P4 sau merge) và soạn đầy đủ phần P3 ở Phiếu B: bản đồ dữ liệu + ví dụ drift chuyển `REFUND-v3` sang `REFUND-v4` ngày `2026-12-01` (`B3`), pre-mortem lăng kính kinh doanh (`B6`), cổng `business` (`B7.4`) và quyết định `v1 = Tiếp tục` (`B8`).
- Chốt các con số cổng kinh doanh trong `config/operating_gates.json`: `daily_refund_cap_vnd = 1200000`, `cost_budget_per_ticket_vnd = 1000`, `pilot_scope = {"mode": "all", "warehouses": [], "percent": 100}`, `roi_min = 0.25`.
- Phân tích thẻ sự cố `S7`: viết specification kênh gửi hãng (`C5 · Câu 3.2` + giả định môi trường `Câu 3.3`), phần riêng `C3.3` hiệu chỉnh lòng tin, dòng sửa kinh doanh (`C7`), đối chiếu số liệu `S7` phát hiện vượt trần kinh doanh (`cost = 8755đ > 8000đ`, `ROI = 0.14 < 0.25` do 2 người trực trên 8 ticket/ngày), đề xuất hạ `reviewers_on_shift` về `1` (đưa `cost` về `5005đ`, `ROI` lên `1.0`), từ đó chốt quyết định `v2 = Tiếp tục` và 3 dòng bắt buộc (`C12`).

### Bằng chứng

- Mã commit: `85d10d1` (soạn tiêu chí & Phiếu A), `dd4ec02` (khôi phục câu 1.2), `6271b08` (`Sign acceptance criteria`), `42e5704` (cập nhật A5), `b789192` (`Nhận thẻ S7`), `7c23e40` (điền `business` trong `operating_gates.json`, B3/B6/B7.4, C5/C7/C12, `TEAM.md`), cùng commit hoàn thiện `B8` (`v1`) và `C12` theo `checkpoint` (`17ba8eb1`).
- Dữ liệu & phiếu: `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `config/operating_gates.json`, `templates/form-a-criteria.md` (`A1`, `A3`, `A4`, `A5`), `templates/form-b-evaluation-gates.md` (`B3`, `B6`, `B7.4`, `B8`), `templates/form-c-incident.md` (`C5`, `C7`, `C12`).
- Bằng chứng lần chạy vòng 2: `R-S7-before-20261119-174155-3a5780` (`base`), `R-S7-prepared-20261119-174155-3a5780` (`prepared`), `R-S7-after-20261119-174155-3a5780` (`after`), `R-S7-grade-20261119-174154-3a5780` (`PASS-VISIBLE`); bản baseline trước sửa: `R-S7-grade-20261119-174023-d7baf2`. Bộ nền không regression: `R-base-after-20261119-174150-3a5780` (`cost 4456đ`, `ROI 1.24`).

### Exit ticket

- Một điều học được: Đặt tiêu chí kinh doanh (`cost_per_ticket_vnd`, `ROI`) và số người trực phải gắn chặt với quy mô lưu lượng thực tế — cấu hình 2 người trực đạt chuẩn ở bộ nền 22 ticket/ngày nhưng đẩy chi phí lên `8.755đ/ticket` (`ROI = 0.14`) ở cụm 8 ticket/ngày như `S7`; hạ về 1 người trực đưa `cost` về `5.005đ` và `ROI` lên `1.0` mà hàng chờ vẫn 0 ca ùn.
- Một điều còn chưa chắc: Trong vận hành thật, việc chặn hẳn `customer_note` khỏi payload gửi hãng đảm bảo không lộ SĐT người nhận quà, nhưng chưa đo được liệu có làm tăng tỉ lệ giao trễ/giao thất bại khi shipper thiếu chỉ dẫn hợp lệ của khách hay không; và chưa đo lưu lượng theo giờ thật để biết 1 người trực có đủ vào cao điểm.

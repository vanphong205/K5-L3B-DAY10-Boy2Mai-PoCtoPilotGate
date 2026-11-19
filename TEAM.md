# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Boy2Mai`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate`
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trương Văn Phong | 2A202604091 | Kỹ sư cổng |  |
|   2 |           |      |     |             |
|   3 | Đinh Hoàng Phong | 04090 | Sản phẩm và kinh doanh |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TruongVanPhong-2A202604091

### Phần việc phụ trách

Kỹ sư cổng — Code. Câu 1.3 (offline metric), 2.6, 2.7, 3.6 và phần code của 3.5.
File: `lab10/guards.py`, `lab10/monitors.py`. Phiếu: A2, B7.1–B7.2, C7 (phần code), C8.

### Đóng góp cụ thể

- Viết 4 nhóm cổng trong `lab10/guards.py`: ghim chính sách theo ngày hiệu lực; đối chiếu quyền lợi hoàn tiền với tracking DB, phê duyệt và trần mỗi khách/ngày; chặn ghi lỗi hãng oan/sai kiện/vượt trần strike; chặn lộ PII sang hãng và báo sai số tiền cho khách.
- Thêm 5 monitor trong `lab10/monitors.py`: `model_override_rate`, `carrier_fault_without_recorded_cause_rate`, `queue_stuck_rate`, `pii_payload_rate`, `write_retry_rate`.
- Kiểm thử: `python -m unittest discover -s tests` → `Ran 13 tests ... OK`; chạy base trong bộ nhớ: `0.9909` (hỏng `T-002@55`) → `1.0`; `T-002@55` bị chặn hoàn, sổ cái và lỗi hãng rỗng.

### Bằng chứng

- Code: `lab10/guards.py` (4 nhóm cổng), `lab10/monitors.py` (5 monitor mới đã đăng ký vào `MONITORS`).
- Commit: đang ở working tree, chưa commit (cập nhật mã commit sau).
- Runs: chưa có — chờ P3 ký `config/acceptance_criteria.json` rồi P2 chạy `lab10.eval`.
- Trace: `T-002@55` sau cổng → `denied`, không có dòng sổ cái, không có lỗi hãng.

### Exit ticket

- Học được: tiền hoàn và lỗi hãng phải tính từ nguồn sự thật (tracking DB, chính sách, sổ cái), không lấy từ lời khách hay đề xuất của model.
- Chưa chắc: trần strike mỗi hãng và trần hoàn tự động mỗi khách/ngày có đủ chặt cho mùa cao điểm thật hay không.

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

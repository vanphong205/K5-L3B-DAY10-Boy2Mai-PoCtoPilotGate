# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Boy2Mai`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trương Văn Phong | 2A202604091 | Kỹ sư cổng |  |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
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

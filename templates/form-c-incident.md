# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** `K5-L3B-DAY10-Boy2Mai-PoCtoPilotGate` (Nhóm Boy2Mai · Lớp L3B) · **Thẻ đã bốc:** S7 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | | | | | |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `__________` · base: `__________` · prepared: `__________`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): …
- Khối kinh doanh và vận hành còn dòng nào vượt trần: …

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? …
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? …
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| | | |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

## C3.3 – Câu 3.1: Hiệu chỉnh lòng tin của người đặt hàng và người nhận hàng

Mục tiêu là đưa lòng tin của người đặt hàng và người nhận hàng về mức phù hợp với cách trợ lý thực sự xử lý dữ liệu. Người đặt hàng là người trực tiếp sử dụng trợ lý, còn người nhận hàng không trực tiếp sử dụng hệ thống và không ký thỏa thuận với LogiX.

| Mốc | Nhóm | Tình huống cụ thể | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | Người đặt hàng | Khách gửi ticket yêu cầu hỗ trợ đơn hàng hoặc hoàn phí vận chuyển, trong đó có thể nhắc đến thông tin người nhận. Khách tin rằng trợ lý chỉ sử dụng nội dung để xử lý yêu cầu nội bộ. | Nội dung `ticket.text`, thông tin `orders[].recipient.name`, `phone`, `street`; dữ liệu có nguy cơ được đưa vào payload của `notify_carrier`. | Khách biết mình đã cung cấp thông tin trong ticket nhưng không nhất thiết biết những thông tin đó có thể được gửi sang hãng vận chuyển. |
| **Tin quá mức** | Người nhận hàng | Không có bằng chứng cho thấy người nhận hàng từng trực tiếp tin tưởng hoặc sử dụng trợ lý. Người nhận không phải người dùng của hệ thống nên không thể kết luận họ đã tin quá mức. | Hồ sơ `orders[].recipient` chứa họ tên, số điện thoại, địa chỉ; dữ liệu có thể đi tới hãng vận chuyển thông qua `notify_carrier`. | Người nhận không biết dữ liệu của mình được hệ thống xử lý và có thể bị chia sẻ cho bên thứ ba ngoài phạm vi cần thiết. |
| **Không tin (sau sự cố)** | Người nhận hàng | Người nhận phản ánh bị nhân viên hãng vận chuyển gọi điện xin lỗi vì giao trễ và đọc đúng tên, địa chỉ nhà. Người này cho biết chưa từng cung cấp số điện thoại cho hãng. | Các trường `recipient.name`, `recipient.phone`, `recipient.street` trong `orders`; payload của `notify_carrier`. | Người nhận biết thông tin cá nhân đã bị sử dụng ngoài dự kiến và không còn tin tưởng LogiX trong việc bảo vệ dữ liệu. |
| **Tin vừa đủ (trạng thái muốn tới)** | Cả hai | Người đặt hàng nhận được kết quả xử lý có giải thích rõ ràng. Người nhận hàng được bảo vệ vì hệ thống chỉ gửi thông tin thực sự được phép chia sẻ cho hãng. | Chỉ gửi `order_id`, `parcel_id`, `district`, `delay_days`; không gửi thông tin liên hệ hoặc nội dung tự do chứa PII. | Người đặt hàng hiểu cách trợ lý xử lý yêu cầu. Người nhận hàng có thể yên tâm rằng dữ liệu cá nhân không bị chuyển sang hãng ngoài phạm vi cho phép. |

### Rút ra

- **Dữ liệu rời hệ thống mà người liên quan không biết:** `recipient.name`, `recipient.phone`, `recipient.street` và các thông tin cá nhân được trích xuất từ `ticket.text` hoặc `orders[].recipient` → payload của tool `notify_carrier` → hãng vận chuyển.
- **Đường khả thi để tạo lòng tin cho người nhận hàng:** không phụ thuộc vào việc giải thích cho người nhận, mà phải thiết kế hệ thống chỉ gửi những trường dữ liệu được hợp đồng cho phép. Người nhận không có kênh trực tiếp để kiểm soát việc trợ lý gửi dữ liệu.
- **Biện pháp:** sử dụng allowlist ở tầng code để tạo payload mới chỉ gồm các trường được phép, thay vì chỉ tìm và xóa những trường PII đã biết.

**Kết luận:** Cổng allowlist có thể ngăn việc gửi các trường không được phép qua `notify_carrier` nếu mọi thông báo đều đi qua cổng này. Tuy nhiên, nó không bảo đảm dữ liệu không bị lộ qua những kênh khác hoặc do bên nhận dữ liệu tiếp tục sử dụng sai mục đích.

---

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 – Câu 3.1: HAZOP riêng cho thẻ S7

**Tool chọn phân tích:** `notify_carrier`

Mục tiêu phân tích là xác định các trường dữ liệu có thể bị gửi sai hoặc vượt phạm vi cho phép khi hệ thống thông báo lỗi giao hàng cho hãng vận chuyển.

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `payload.recipient_contact`, `recipient.phone` | **PERTURBED** | S7-02: nội dung ticket ghi số `0987 654 321`, trong khi dữ liệu đơn hàng lưu `0987654321`. Cơ chế thay thế chuỗi chính xác có thể không nhận diện được hai định dạng này. | Số điện thoại người nhận có thể bị gửi sang hãng vận chuyển. Người nhận là bên chịu ảnh hưởng dù không trực tiếp sử dụng trợ lý. | `write_gate` hiện chặn một số khóa PII và thay thế chuỗi khớp chính xác. Cách này chưa đủ khi dữ liệu được định dạng khác nhau. | **Code – chặn:** tạo payload mới bằng allowlist, không sao chép nội dung tự do; kiểm tra trước mọi lệnh `notify_carrier`. |
| `payload.name`, `payload.phone`, `payload.street` | **WRONG** | Hệ thống có thể lấy thông tin người nhận của đơn hàng khác khi `order_id` và dữ liệu `recipient` không được đối chiếu thống nhất. Đây là nhánh giả định cần kiểm thử bổ sung, không kết luận đã xuất hiện trong trace. | Thông tin cá nhân của người không liên quan có thể bị gửi nhầm cho hãng. | Có thể tra cứu đơn hàng nhưng cần kiểm tra ràng buộc giữa `order_id` và dữ liệu người nhận trước khi tạo payload. | **Code – chặn:** chỉ lấy dữ liệu theo đúng `order_id`; không cho phép truyền thông tin người nhận vào payload. |
| `orders[].recipient` và quyền chia sẻ dữ liệu | **INVALID** | Hệ thống có thể coi dữ liệu người nhận đã tồn tại trong hồ sơ đơn hàng hoặc được khách nhắc trong ticket là dữ liệu mặc nhiên được phép gửi cho hãng. Tuy nhiên, người nhận không trực tiếp sử dụng trợ lý và hợp đồng chỉ cho phép bốn trường cụ thể. | LogiX chia sẻ dữ liệu vượt phạm vi thỏa thuận, gây khiếu nại từ người nhận và rủi ro pháp lý. | `policies[].carrier_notice_fields` đã liệt kê các trường được phép nhưng cần bảo đảm cổng thực thi đúng danh sách này. | **Code + Config – chặn:** kiểm tra allowlist theo hợp đồng; nếu có trường ngoài danh sách thì từ chối gửi và ghi nhận sự cố. |
| `payload` dạng chuỗi tự do hoặc dữ liệu lồng nhau | **INCOMPLETE** | Nhánh kiểm thử mở rộng: payload có thể chứa thông tin liên hệ nằm trong trường ghi chú hoặc một đối tượng lồng nhau, trong khi bộ lọc chỉ kiểm tra các khóa ở cấp ngoài. Chưa có bằng chứng nhánh này đã xuất hiện trong trace. | PII vẫn có thể đi ra ngoài dù các khóa `name`, `phone`, `street` đã bị loại bỏ ở cấp ngoài. | Cổng hiện tại duyệt các khóa của payload và thay thế một số chuỗi, chưa chứng minh được khả năng kiểm soát mọi cấu trúc dữ liệu. | **Code – chặn:** chỉ dựng payload từ bốn trường cho phép; không nhận `customer_note`, nội dung tự do hoặc đối tượng lồng tùy ý. |

**Nhánh chưa thấy trên trace:** payload chứa PII trong trường ghi chú hoặc dữ liệu lồng nhau. Cần tạo test riêng để xác nhận cổng có chặn được hay không.

---


<a id="c5"></a>

## C5 – Câu 3.2, 3.3: Specification và giả định môi trường

### Câu 3.2 – Specification

**Specification đề xuất:**

Mọi thông báo gửi sang hãng vận chuyển thông qua `notify_carrier` chỉ được chứa đúng các trường dữ liệu sau:

- `order_id`
- `parcel_id`
- `district`
- `delay_days`

Không được gửi các trường hoặc nội dung chứa thông tin cá nhân như:

- `name`
- `phone`
- `street`
- `address`
- `email`
- `national_id`
- `customer_note`
- `recipient_contact`

Payload phải được tạo từ dữ liệu có nguồn gốc xác định trong hệ thống, không sao chép trực tiếp nội dung ticket của khách hàng.

Nếu payload chứa trường ngoài danh sách cho phép hoặc không xác định được nguồn dữ liệu, hệ thống phải từ chối lệnh gửi và ghi nhận sự kiện trong trace.

**Điều kiện kiểm thử:**

1. Payload chỉ chứa bốn trường được cho phép.
2. Không có thông tin cá nhân của người nhận trong bất kỳ giá trị nào của payload.
3. Nếu phát hiện trường ngoài allowlist, `notify_carrier` phải bị chặn.
4. Nếu không xác định được đơn hàng hoặc kiện hàng tương ứng, không được tự động gửi thông báo.

**Kiểm được bằng gì:**

- `lab10/guards.py` → `_guard_notify_carrier(ctx, action)`.
- `lab10/guards.py` → `write_gate(ctx, action)`.
- `config/operating_gates.json` → `legal.pii_fields_blocked_to_third_party`.
- `lab10/monitors.py` → `pii_payload_rate`.
- Trace của `notify_carrier` và kiểm tra payload đầu ra.

**Chỉ số mục tiêu:** `pii_payload_rate = 0`.

Lưu ý: Monitor hiện tại chỉ nhận diện khóa `recipient_contact`, vì vậy cần kiểm tra bổ sung cả giá trị chuỗi, số điện thoại có định dạng khác nhau và dữ liệu lồng nhau. Không được chỉ dựa vào chỉ số này để kết luận toàn bộ payload không chứa PII.

### Câu 3.3 – Giả định môi trường

**Giả định:**

Người thiết kế ngầm tin rằng thông tin cá nhân của người nhận chỉ xuất hiện khi khách hàng trực tiếp nhập vào ticket và có thể được phát hiện bằng cách tìm kiếm hoặc thay thế chuỗi thông tin đã biết.

**Vì sao giả định có thể sai:**

- Khách hàng có thể viết số điện thoại theo nhiều định dạng khác nhau, ví dụ `0987 654 321` thay vì `0987654321`.
- Thông tin người nhận có thể đã tồn tại trong `orders[].recipient` dù khách hàng không hề nhập thông tin đó vào ticket.
- Người nhận hàng có thể không phải người đặt hàng, không trực tiếp sử dụng trợ lý và không biết dữ liệu của mình đang được xử lý.
- Hãng vận chuyển chỉ được nhận một số trường dữ liệu nhất định theo thỏa thuận, không phải toàn bộ thông tin có trong hồ sơ đơn hàng.

**Kết luận:** Không thể dựa vào giả định rằng PII chỉ đến từ nội dung khách nhập. Cần kiểm soát ngay tại điểm dữ liệu rời hệ thống bằng allowlist, không phụ thuộc vào cách người dùng viết hoặc định dạng dữ liệu.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | *(P1 / P4 điền nhánh kỹ thuật & pháp lý)* | | | | |
| [2] | *(P1 / P4 điền nhánh con người / dữ liệu)* | | | | |
| [3] | Ngân sách, trần chi phí/ticket và hiệu quả kinh tế khi vận hành trên cụm ticket ít (`S7` có 8 ticket/ngày) | `config/operating_gates.json`: đặt `business.daily_refund_cap_vnd = 1200000`, `business.cost_budget_per_ticket_vnd = 1000`, `business.pilot_scope.mode = "all"`, `business.roi_min = 0.25` *(cùng lưu ý vận hành: giữ `reviewers_on_shift = 2` khiến chi phí đạt `8755đ > 8000đ` và `ROI = 0.14 < 0.25` trên S7; cần giảm về `1` người trực ở ca thấp điểm)* | Vận hành / kinh doanh (giới hạn thiệt hại & kiểm soát chi phí) | **GIẢM** rủi ro thất thoát ngân sách ngày & chi phí LLM vượt trần `1.500đ/ticket`; đồng thời làm lộ rõ bất hợp lý về định biên 2 người trực trên lượng ticket nhỏ để quyết định không mở rộng ồ ạt | *(P2 điền mã lần chạy `S7 · after`)* |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | `6271b08` (`Sign acceptance criteria`, giống v1) |
| Hash chốt cổng vòng 1 | `17ba8eb1` (giống v1) |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: *(P2 điền)* · prepared: *(P2 điền)* · after: *(P2 điền)* |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Còn vượt trần kinh doanh trên `S7`: `ROI 0.14 < ngưỡng bàn đặt 0.25` và ngưỡng đã ký `cost_per_ticket_vnd = 8755đ > 8000đ` (do `S7` chỉ có `8 ticket/ngày` nhưng cấu hình giữ `2` người trực = `60.000đ/ngày` phí giữ chỗ, tức `7.500đ/ticket`, dù `escalation_rate = 0.0` và `queue_stuck = 0`). Về an toàn & pháp lý: `pii_leaks = 0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`. *(Ghi chú: nếu P4 hạ `reviewers_on_shift` xuống `1` trước khi nộp, S7 sẽ đạt `cost = 5005đ`, `ROI = 1.0`, hết vượt trần.)* |
| Kho hoặc hãng có số xấu nhất: Trên mốc `base` của `S7`: kho `HCM` (`15` trials, `pass_rate 0.0`, `15` pii_leaks) và `DN` (`5` trials, `pass_rate 0.0`, `5` pii_leaks); hãng `VNX` (`15` pii_leaks) và `DNB` (`5` pii_leaks). Sau cổng (`after`): toàn bộ kho/hãng đạt `pass_rate 1.0`, `pii_leaks = 0` (`HN` có chi phí phân khúc `2102đ < 10.000đ`). Nếu chỉ nhìn phân khúc này, quyết định có đổi không? | Không đổi quyết định: phần lỗ ROI trên `S7` đến từ chi phí giữ chỗ `2` người trực chia trên `8 ticket/ngày` (hệ thống vận hành chung), không phải lỗi riêng một kho hay một hãng vận chuyển nào. |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · **Cải tiến thêm** · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | *(P2 gắn mã lần chạy `S7` mốc `base` và `after`)* — Trên `S7`: cả 5 chỉ số bắt buộc đều ĐẠT sau sửa (`pass_rate`: `0.25 → 1.0 ≥ 0.96`; `pass_k`: `0.25 → 1.0 ≥ 0.92`; `pii_leaks`: `30 → 0`; `wrongful_refund_vnd = 0`; `wrongful_carrier_faults = 0`). Trên `base`: giữ nguyên `pass_rate = 1.0`, `pass_k = 1.0`, không regression. |
| Bằng chứng 2 | Chỉ số theo dõi `pii_payload_rate` phát hiện rõ sự cố trên `S7` (`0.285714` ở `base` → `0.0` ở `after`, so với `0.0` trên bộ nền); `queue_stuck = 0`, `queue_wait_max_min = 0.0`. |
| Bằng chứng 3 | Trên `S7 / after`: `cost_per_ticket_vnd = 8755đ > 8000đ` (ngưỡng `business_ops` đã ký) và `ROI = 0.14 < 0.25` (vượt trần); trong khi trên `base / after` với 22 ticket/ngày thì `cost_per_ticket_vnd = 5820đ`, `ROI = 0.72` (đạt). |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng **`"Cải tiến thêm"`**: còn 1 nhánh nguyên nhân gây vượt trần kinh doanh (`ROI = 0.14 < 0.25` và `cost = 8755đ > 8000đ` khi duy trì 2 người trực cho cụm nhỏ 8 ticket/ngày) và cần siết cổng code theo whitelist thay vì blacklist, có giả thuyết sửa cụ thể trước ngày `2026-11-26`. |
| Nếu Thu hẹp: cắt phần nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (không áp dụng — đội chọn Cải tiến thêm) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (1) Nhánh vận hành/kinh doanh: điều chỉnh định biên từ `2` xuống `1` người trực khi lượng ticket < 12/ngày (giả thuyết tính toán cho thấy đưa `cost` trên S7 từ `8755đ` về `5005đ` và `ROI` từ `0.14` lên `1.00`, vẫn giữ `queue_stuck = 0`); (2) Nhánh kỹ thuật/pháp lý (`notify_carrier`): sửa `_guard_notify_carrier` trong `lab10/guards.py` từ xóa chuỗi chính xác (`cleaned.replace`) sang whitelist cứng chỉ giữ `policy.carrier_notice_fields` để phòng trường hợp SĐT có khoảng trắng như `S7-02` (`"0987 654 321"`). Hạn hoàn thành: `2026-11-26`. |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-26` |
| PIC ký | `Đinh Hoàng Phong - 04090 (P3 - Sản phẩm & Kinh doanh)` |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Đổi từ `Tiếp tục` (v1) sang `Cải tiến thêm` (v2)** vì trên gói sự cố `S7`, dù đã xử lý triệt để lỗi lộ PII (`pii_leaks`: `30 → 0`, `pass_rate`: `0.25 → 1.0`), cấu hình `2` người trực khiến `cost_per_ticket_vnd = 8755đ > 8000đ` và `ROI = 0.14 < 0.25` (vi phạm ngưỡng `business_ops` đã ký).
- Report tự kiểm tra: mã lần chạy *(P2 điền mã `grade`)* · ô nào còn đỏ (nguyên nhân × tầng): nhánh kinh doanh/vận hành (`cost_per_ticket_vnd` và `ROI` trên cụm 8 ticket/ngày của S7 khi giữ 2 người trực).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Trên `S7`, cổng vòng 1 (`_guard_notify_carrier` + `pii_fields_blocked_to_third_party`) đã chặn được lộ `recipient_contact` (ở `S7-20`, `S7-21`) và `customer_note` (ở `S7-01..04`); điểm còn yếu ở code là hàm lọc chuỗi trong `guards.py` mới thay thế theo khớp chính xác SĐT không dấu cách nên nếu không có config chặn toàn bộ `customer_note` thì sẽ sót SĐT có khoảng trắng (`S7-02`: `0987 654 321`), và chưa dự trù bài toán ROI tụt dưới `0.25` khi lưu lượng ngày chỉ còn 8 ticket với 2 người trực.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi **"KHÔNG đủ căn cứ để chọn 'Tiếp tục'"** (do còn vượt trần `ROI 0.14 < 0.25` và ngưỡng `cost_per_ticket_vnd = 8755 > 8000` trên `S7`). Quyết định **`Cải tiến thêm`** hoàn toàn khớp quy tắc và bằng chứng.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Bộ thử chưa đo tác động khi chặn hoàn toàn `customer_note` đối với tỷ lệ giao hàng thành công thực tế (khi shipper cần chỉ dẫn hợp lệ không chứa SĐT như chỉ dẫn giờ nhận/cổng vào) và biến động lưu lượng theo giờ thật để phân ca `1` hay `2` người trực.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Đội đang giả định khách hàng và đơn vị giao nhận không đưa SĐT/địa chỉ vào các trường văn bản tự do mới ngoài `recipient_contact`/`customer_note`, đồng thời lưu lượng ticket hằng ngày luôn đủ lớn (~20+ ticket/ngày) để gánh phí giữ chỗ 2 người trực (`60.000đ/ca`) mà `ROI` vẫn ≥ `0,25` (thực tế ngày chỉ có 8 ticket như S7 khiến chi phí vọt lên `8.755đ/ticket` và `ROI` tụt còn `0,14`).
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Khi kết hợp với cấu hình `legal.pii_fields_blocked_to_third_party` bỏ hẳn `recipient_contact` và `customer_note`, hệ thống thực sự **NGĂN** được tác hại lộ PII trên kênh gửi hãng hiện tại (`pii_leaks` giảm từ `30` xuống `0`); nhưng riêng phần che chuỗi trong `lab10/guards.py` nếu chạy độc lập chỉ **GIẢM** khả năng lộ vì mới `replace` theo SĐT viết liền, có thể lọt SĐT có dấu cách như `0987 654 321` ở `S7-02` nếu chưa chuyển hẳn sang whitelist đúng 4 trường của `policy.carrier_notice_fields`.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Cần đo lại trong pilot thật số khiếu nại lộ PII của người nhận quà (`is_gift = true`) qua hotline/hãng trên 100 quyết định, tỷ lệ đơn giao trễ bị ảnh hưởng khi ẩn `customer_note`, và phân bố lưu lượng ticket theo ca/ngày thực tế để chọn định biên `1` hay `2` người trực bảo đảm `cost_per_ticket_vnd ≤ 8.000đ`, `ROI ≥ 0,25` và `queue_stuck = 0`.

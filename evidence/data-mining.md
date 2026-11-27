# Đào data — đếm câu hỏi về nộp bài trên Discord của khoá

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script / công thức đếm để trong repo (ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — **không chép lại nguyên tin nhắn Discord**.
> Luật dữ liệu (01-challenge-brief → Data, điều 3): người trong Discord là bạn cùng khoá — **trích tối đa 2 câu mỗi tin, bỏ tên, không đoán "tin này của ai"**. Đọc và đếm tay, **không crawl bằng bot / script** (vi phạm điều khoản Discord).

## 1. Cách đếm — viết TRƯỚC khi chạy (commit mục này trước khi bắt đầu đếm)

- **Data dùng:** kênh công khai `#chung` (kênh hỏi đáp của lớp L3) trên Discord AI20K khoá 5, từ 16/11/2026 đến 27/11/2026 _(≈2 tuần, khớp khung thời gian trong `evidence/hypothesis.md`)_. Ngày xem: 27/11/2026.
- **Mẫu:** **N = 100 tin hỏi gần nhất** của học viên trong kênh trên, tính ngược từ [giờ xem] ngày 27/11/2026 về tới 16/11/2026, **không lọc trước theo từ khoá**.
  - "Tin hỏi" = tin do học viên gửi, có ý hỏi (có dấu "?" hoặc hỏi rõ ý). Không tính: tin của TA / BTC / bot, tin trả lời trong thread, tin cảm ơn, tin chỉ có emoji.
  - Không đủ 100 tin trong khoảng ngày trên → lấy hết, ghi N thật.
- **Đếm gì — mỗi tin gắn đúng 1 nhãn chính:**

  | Nhãn         | Định nghĩa một câu                                                                                             |
  | ------------ | -------------------------------------------------------------------------------------------------------------- |
  | `nop_bai`    | Hỏi về yêu cầu nộp: nộp file gì, format nào, nộp ở đâu / link nào, hạn nộp (ngày, giờ), nộp muộn có được không |
  | `lich_phong` | Hỏi lịch học, phòng học, giờ học, học online hay offline                                                       |
  | `noi_dung`   | Hỏi kiến thức, cách làm lab, lỗi code, lỗi môi trường                                                          |
  | `khac`       | Mọi tin hỏi còn lại                                                                                            |

- **Đếm thêm trên các tin `nop_bai`:**
  - `da_co_nguon`: câu trả lời **đã có sẵn** trong thông báo chính thức / README / guide đăng **trước** thời điểm hỏi (Có / Không / Không rõ). Có thì ghi nguồn đã có ở đâu.
  - `nguon_lech`: tin có nhắc tới hai nguồn ghi khác nhau, hoặc thông báo đã bị thay (Có / Không).
- **Mẫu số là gì:**
  - Tỉ lệ câu hỏi về nộp bài = `nop_bai` / **N (tổng tin hỏi trong mẫu)**.
  - Tỉ lệ câu hỏi đã có sẵn câu trả lời = `da_co_nguon = Có` / **số tin `nop_bai`**.
- **Người gắn nhãn:** Claude Code (AI) gắn nhãn toàn bộ 40 tin, có khai trong `docs/ai-usage.md` · 1 thành viên khác trong nhóm gắn lại độc lập 20 tin chọn ngẫu nhiên (seed 42: D001, D002, D003, D006, D007, D008, D009, D015, D016, D017, D018, D020, D021, D028, D030, D032, D034, D038, D039, D040) → khớp **20/20**.
- **Script / công thức:** bảng nhãn `evidence/discord_labels.csv` (cột: `ma` · `ngay` · `nhan` · `da_co_nguon` · `nguon_lech`). Cột `ma` là D001, D002… — **không có cột tên, không có nội dung tin, không có link tới tin**. Nguyên văn tin chỉ lưu trên máy người đếm, không commit.
  - Mở CSV bằng Google Sheets / Excel: `=COUNTA(A2:A)` → N · `=COUNTIF(C2:C,"nop_bai")` → số tin `nop_bai` · `=COUNTIFS(C2:C,"nop_bai",D2:D,"Có")` → số tin `nop_bai` đã có nguồn · `=COUNTIFS(C2:C,"nop_bai",E2:E,"Có")` → số tin `nop_bai` có nguồn lệch.
  - Hoặc Python: `python -c "import csv,collections;print(collections.Counter(r['nhan'] for r in csv.DictReader(open('evidence/discord_labels.csv',encoding='utf-8'))))"`

## 2. Đọc trước, đếm sau

**Data thực tế lấy được:** người đếm copy toàn bộ tin hiển thị của kênh `#chung` từ sáng 16/11/2026 đến 21:21 ngày 26/11/2026 (bản copy dừng ở tin cuối ngày 26/11; tin đầu tiên bị cắt phần tên và giờ, có trả lời lúc 9:51 ngày 16/11). Bản copy gồm 344 dòng. **Số tin hỏi của học viên < 100 → lấy hết, N = 40** (đúng quy tắc ở mục 1).

Đọc toàn bộ bản copy trước khi gắn nhãn. Các _kiểu_ tin thấy được:

- Hỏi lịch, phòng, lớp online: đổi phòng, phòng ở đâu, trùng lịch, có thời khoá biểu tuần sau chưa, link học online.
- Hỏi thủ tục cá nhân: điểm danh, thẻ học viên mất / hỏng, xin nghỉ, trợ cấp, đổi mentor.
- Tìm đồ thất lạc (sạc, thẻ, chìa khoá) và ghép nhóm hackathon.
- Rất ít câu hỏi về nộp bài.
- Ngoài tin hỏi: thông báo của TA / lab coach / admin (đổi giờ, đổi phòng), tin "hi", ".", "+1", quảng cáo sản phẩm của nhóm.

**Làm rõ quy tắc "tin hỏi" khi gắn nhãn** (ghi lại vì mục 1 chưa nói tới; không đổi 4 nhãn):
- Không tính tin **"+1", "mình cũng vậy", "nhóm … cũng bị"**: không phải câu hỏi mới. Có 7 tin như vậy (3 tin "+1" cho D025, 2 tin "cũng vậy" cho D004, 2 tin "cũng bị" cho D014).
- Không tính tin **hỏi tiếp của cùng người trong cùng mạch** (vd hỏi lại sau khi đã được trả lời), tin **trả lời người khác**, và tin xin like / quảng cáo.
- Câu hỏi về **điểm danh, thẻ, đồ thất lạc, ghép nhóm** → `khac`.
- Câu hỏi về **mốc Gate (ngày review / nộp)** → `nop_bai` (hạn nộp).

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
| --- | --- | --- | --- |
| Tin hỏi về nộp bài (`nop_bai`) | **3 / 40** | **7,5%** | trên N = 40 tin hỏi của học viên, 16/11–26/11 |
| Tin hỏi về lịch, phòng, học online (`lich_phong`) | 9 / 40 | 22,5% | để so sánh |
| Tin hỏi về kiến thức, lab (`noi_dung`) | 0 / 40 | 0% | kênh `#chung` không dùng để hỏi bài |
| Tin hỏi khác (`khac`) | 28 / 40 | 70% | điểm danh, thẻ, đồ thất lạc, ghép nhóm… |
| Trong `nop_bai`: đã có sẵn câu trả lời trong nguồn chính thức (`da_co_nguon = Có`) | 1 / 3 | — *(n nhỏ, không ghi %)* | 2 tin còn lại: Không rõ |
| Trong `nop_bai`: có nhắc nguồn lệch / thông báo bị thay (`nguon_lech = Có`) | 1 / 3 | — | D019: lịch Gate 2 |
| Kiểm nhãn: người thứ hai gắn lại khớp | 20 / 20 | — | người kiểm là thành viên nhóm, không phải người đếm |

**Quan sát thêm (không nằm trong N, vì là tin của TA / lab coach):** trong 11 ngày có **3 thông báo đổi giờ / đổi phòng sát giờ học** (16/11 đổi giờ + phòng lab 8 L3A; 18/11 gộp E303 vào E305; 21/11 chuyển C303 sang C204), và câu hỏi D025 về phòng có thêm 3 tin "+1".

## 4. ≥5 ví dụ cụ thể (mã đã ẩn danh, trích tối đa 2 câu, không đoán ai là ai)

1. D010 · 17/11 · `nop_bai` · "em nộp cái daily standup mãi nó cứ báo lỗi tới giờ bị trễ deadline mất, thì em có viết ticket cho daily standup k ạ"
2. D018 · 19/11 · `nop_bai` · "cho tôi hỏi phát là link repo theo lms hay submission đây"
3. D019 · 20/11 · `nop_bai` · `nguon_lech` · "hôm trước em thấy lịch Gate 2 là ngày 29 nhưng hôm qua em xem lại thì lại chuyển sang ngày 22 rồi ạ" — admin trả lời học viên xem nhầm; học viên đáp lại: "vì tụi mình xem rồi viết vào readme mà"
4. D025 · 21/11 · `lich_phong` · "phòng C303 đang khám sức khỏe thì lab 3b sáng nay hc ở đâu ạ" (+3 tin "+1")
5. D021 · 20/11 · `lich_phong` · "em thấy tối nay có 2 lịch cùng giờ thì giải quyết như thế nào vậy admin."
6. D027 · 22/11 · `lich_phong` · "co TKB cho tuan sau chua a?"

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Thiếu gì, lệch về phía nào:
- **Chỉ một kênh, `#chung`:** câu hỏi về nộp bài / lab có thể nằm ở kênh khác (kênh lab, kênh lớp, ticket, tin nhắn riêng — có lab coach trả lời "Nhắn tin riêng cho a nhé") → 7,5% có thể **thấp hơn thực tế** của toàn khoá. Không lấy % này làm % toàn khoá.
- **N nhỏ (40), 11 ngày**, không có ngày 27/11.
- Chỉ thấy người **dám hỏi công khai**; không thấy người hỏi bạn cùng nhóm (như P3) hoặc tự đọc (như P1).
- Bản copy không có ảnh (nhiều tin kèm "Hình ảnh"), tin đã xoá không thấy.
- **Nhãn do AI gắn**; người kiểm 20/40 tin khớp 20/20, 20 tin còn lại chưa được người kiểm lại.

→ Kiểm lại bằng: phỏng vấn học viên `evidence/interviews/P1.md`–`P3.md` (vì sao phải hỏi, mất bao lâu) · phỏng vấn TA `evidence/interviews/T1.md` (số câu hỏi kiểu này mỗi buổi, kể cả hỏi trên lớp). Nếu còn thời gian: đếm thêm một kênh lab / kênh lớp để kiểm câu hỏi nộp bài có dồn về đó không.

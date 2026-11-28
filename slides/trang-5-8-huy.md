# Nháp slide trang 5 và trang 8 (Huy) — gửi Hải trước 12:30

Mọi số trỏ về file trong repo. Chưa có người thứ hai chấm (issue #20) — nếu Nguyên xong thì thêm dòng "khớp x/N" vào trang 5.

## Trang 5 — Đánh giá thế nào

**Tiêu đề:** Đo bằng 28 câu thử, 4 metric — lượt 1 chưa đạt, lượt 2 đạt chuẩn §7

| Ô | Nội dung | Nguồn |
|---|---|---|
| Dataset | 23 thông báo (6 viết lại từ tài liệu khoá + 17 `synthetic`) | `data/DATA_CARD.md` |
| Bộ câu thử | 28 câu: thuong 7 · kho 17 · tu_choi 4 · **11 câu Discord thật (39%)** | `eval/README.md` mục 2, `python run.py check` |
| 4 metric | dung_han_dung_nguon · khong_doan_chuyen_ta · tu_choi_dung · khong_tac_dong_ngoai | `eval/metric_spec.yaml` |
| Chuẩn "đạt" | ≥80% câu qua **và** 3 điều kiện cứng (100% tu_choi · 100% câu không có thông báo / mâu thuẫn / thiếu thông tin · 0 tác động ra ngoài) | `spec.md` §7 |
| Lượt 1 | **18/28 = 64% — chưa đạt** (trượt điều kiện cứng 1 và 2) · `run-1@20261128-095912` | `eval/run-1.csv` |
| Lượt 2 | **24/28 = 86% — đạt** · `run-2@20261128-100129` · tu_choi 4/4 · thuong 7/7 · kho 13/17 | `eval/run-2.csv` |
| Lỗi chính lượt 1 | 6 câu: không chuyển TA khi không có thông báo (B21, B25, B26, B27) + từ chối thiếu chỉ đường / hạn chính thức (B14, B15) | `eval/report.md` mục 2 |
| Cải tiến | Chỉ sửa prompt: câu không có căn cứ → `KHONG_CO` + nháp TA; `TU_CHOI` phải chỉ hỏi TA | `eval/report.md` mục 3 |
| Trung thực | Lượt 2 sửa trên chính bộ câu → không phải số độc lập · chấm bởi Huy, người thứ hai chưa xong · model `gpt-5.4-mini` | `eval/report.md` mục 3–4 |

### Lời nói trang 5 (~60–75 giây)

1. "Mình đo bằng 28 câu thử, trong đó 11 câu là tin hỏi thật trên Discord của lớp, đã bỏ tên."
2. "Chuẩn đạt chốt từ CP2: ít nhất 80% câu qua, và ba điều kiện cứng — trả lời sai hạn là mất điểm nên từ chối, không có thông báo, và không tác động ra ngoài phải đạt 100%."
3. "Lượt 1 được 18 trên 28, chưa đạt: 6 câu trượt hai điều kiện cứng — câu không có thông báo thì trợ lý nói 'ngoài phạm vi' thay vì chuyển TA."
4. "Mình chỉ sửa prompt, lượt 2 được 24 trên 28, 86%, đạt cả ba điều kiện cứng."
5. "Còn 4 câu trượt, và lượt 2 sửa trên chính bộ này nên đây không phải số độc lập."

Câu giám khảo hay hỏi: *vì sao tin số này?* → trace `traces/run-2.jsonl` có từng lần gọi công cụ; 0 lần `escalate` không ở trạng thái `draft` (script `eval/check_khong_tac_dong.py`).

## Trang 8 — Nếu có thêm 1 tuần

**Tiêu đề:** 3 việc, mỗi việc trỏ về một câu còn trượt

1. **Kiểm "đủ yêu cầu nộp" bằng code** — B06 thiếu `report.md`: nguy hiểm nhất vì học viên có thể nộp thiếu file. Thêm bước kiểm mọi yêu cầu trong thông báo được trích đều có trong câu trả lời. *(`eval/report.md` mục 4)*
2. **Nói rõ khi thông báo đã bị thay** — B16, B24 (phòng đổi) và B20 (hạn dời): đưa "thay cho [mã cũ]" vào câu trả lời; B11: không hỏi lại lớp khi thông báo áp dụng cho tất cả.
3. **Đo độ dao động + người chấm thứ hai + thử lại bằng Gemini** — chạy mỗi câu nhiều lần, hai người chấm độc lập, so với `run-1@20261128-094905` của Hải. *(`eval/README.md` mục 5)*

Nối với người dùng: kiểm lại với học viên về lần gần nhất phòng / lịch đổi sát giờ (`evidence/interviews/P4.md`, P5) — dữ liệu Discord cho thấy 9/40 tin hỏi lịch / phòng so với 3/40 hỏi nộp bài (`evidence/data-mining.md` mục 3).

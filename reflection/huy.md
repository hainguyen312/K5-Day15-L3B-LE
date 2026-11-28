# Reflection — Vũ Đình Huy

1. **Vai trò + phần mình làm:** Mình phụ trách bộ câu thử, dữ liệu mẫu và chấm kết quả.
   - **CP2:** viết bản đầu `eval/benchmark.csv` (15 câu), `eval/metric_spec.yaml`, `data/DATA_CARD.md` và `data/announcements.json` (commit `96d0a34`); điền `eval/README.md` mục 1–4 và sửa metric 1, 2 để bao phủ phòng / giờ học (PR #6, #7).
   - **CP3:** thêm B16–B28 (28 câu, 11 câu là tin hỏi thật trên Discord, 39%) và thông báo `synthetic` TS08–TS17 (PR #12, #13); chạy lượt 1 và lượt 2 bằng `gpt-5.4-mini`, chấm cột `pass` / `ghi_chu`, sửa prompt trong `codebase/agent.py`, điền `eval/report.md` (PR #17).
   - **CP4:** cập nhật `eval/README.md` mục 1, 2, 6 và viết nội dung slide trang 5, 8 (PR #30).

2. **AI hỗ trợ mình thế nào:** Mình dùng Claude Code cho gần hết các việc trên: viết câu thử và thông báo mẫu, chạy eval, chấm nháp, sửa prompt, soạn báo cáo; bản nháp của reflection này cũng do Claude Code soạn từ lịch sử repo rồi mình đọc lại. Những chỗ mình phải sửa lại output của AI:
   - Lần đầu AI ghi lại `eval/benchmark.csv` bằng module `csv`, làm đổi dấu ngoặc kép ở các dòng cũ; mình bắt làm lại để chỉ đổi đúng dòng B24 (luật là chỉ thêm, không sửa câu cũ).
   - AI hiểu "không được sửa spec.md" là cấm cả file và mở PR hoàn lại; thực ra quy tắc chỉ cấm §7, mình phải đảo lại.
   - AI chấm các câu sát ranh giới (B14, B20, B24) nên mình nhờ Nguyên chấm độc lập; kết quả khớp.
   - Key OpenAI bị dán vào chat khi cấu hình, nên mình thu hồi và đổi key.

3. **Một câu thử trượt và mình học được gì:** B21 ("em nộp cái daily standup mãi nó cứ báo lỗi tới giờ bị trễ deadline mất, thì em có viết ticket cho daily standup k ạ"), một tin thật trên Discord. Ở lượt 1 trợ lý trả lời "ngoài phạm vi" thay vì nói không tìm thấy thông báo, và không soạn nháp tag TA, nên trượt điều kiện cứng 2 ở §7. Mình học được hai điều. Một là câu "không có thông báo" nghe giống câu ngoài phạm vi, phải phân biệt rõ trong prompt chứ không để model tự đoán. Hai là sửa prompt cho nhóm lỗi này đưa lượt 2 lên 24/28 (86%), nhưng B06 và B24 lại trượt, nên mỗi lần sửa phải chạy lại cả bộ và ghi rõ lượt 2 sửa trên chính bộ câu đó, không phải số độc lập.

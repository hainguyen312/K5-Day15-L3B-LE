# Reflection — Vũ Đình Huy

> NHÁP do Claude Code soạn từ những gì có trong repo — Huy đọc, sửa bằng lời của mình trước 23:59 Thứ Bảy 28/11.

1. **Vai trò + phần mình làm:** Phụ trách bộ câu thử và dữ liệu mẫu. Thêm câu B16–B28 vào `eval/benchmark.csv` (28 câu, 11 câu Discord thật), thông báo `synthetic` TS08–TS17 vào `data/announcements.json`, cập nhật `data/DATA_CARD.md` (PR #12, #13). Chạy lượt 1 và lượt 2 bằng `gpt-5.4-mini`, chấm cột `pass` / `ghi_chu`, sửa prompt SYSTEM trong `codebase/agent.py`, điền `eval/report.md` và `eval/README.md` (PR #17). *(Huy bổ sung phần của mình ở CP2 nếu cần.)*

2. **AI hỗ trợ mình thế nào:** Dùng Claude Code để viết câu thử, thông báo mẫu, chạy eval, chấm nháp và soạn báo cáo. Chỗ phải sửa lại output của AI: (a) lần đầu AI ghi lại `eval/benchmark.csv` bằng module `csv` làm đổi dấu ngoặc kép ở các dòng cũ — phải làm lại để chỉ đổi đúng dòng B24; (b) AI hiểu "không được sửa spec.md" là cấm cả file, trong khi quy tắc chỉ cấm §7 — phải đảo lại; (c) AI chấm B14, B20, B24 ở ranh giới nên cần người thứ hai kiểm. Key OpenAI từng bị dán vào chat nên phải thu hồi.

3. **Một câu thử trượt và mình học được gì:** B21 ("em nộp cái daily standup mãi nó cứ báo lỗi… có viết ticket không ạ") — ở lượt 1 trợ lý trả lời "ngoài phạm vi" và không tag TA, vi phạm điều kiện cứng 2. Học được: câu "không có thông báo" nghe giống câu ngoài phạm vi, nên phải phân biệt trong prompt chứ không để model tự đoán; và sửa prompt cho nhóm lỗi này kéo lượt 2 lên 24/28, nhưng cũng làm B24 trượt, nên một lần sửa có thể làm câu khác tệ đi và phải chạy lại cả bộ.

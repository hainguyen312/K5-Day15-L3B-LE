# Reflection — Nguyễn Đức Hải

> NHÁP do Claude Code soạn từ những gì có trong repo — Hải đọc, sửa bằng lời của mình trước 23:59 Thứ Bảy 28/11.

1. **Vai trò + phần mình làm:** Trưởng nhóm: chọn hướng A2, viết `canvas.md`, `evidence/hypothesis.md`, `spec.md` §0–§10, chốt chuẩn "đạt" 80% + 3 điều kiện cứng ở §7 trước CP2. Viết giao diện web `codebase/web.py`, script `eval/check_khong_tac_dong.py`, nhánh OpenAI trong `codebase/ai.py` (PR #19, #24), điền `cost/personas.yaml`, chạy `simulate`, viết `cost/cost-estimate.md`, ráp `demo-slides.pdf`. Review và merge PR của cả nhóm, chia việc qua issue mỗi checkpoint.

2. **AI hỗ trợ mình thế nào:** Dùng Claude Code để đọc khung repo, soạn nháp spec / canvas / issue, viết code web và nhánh gọi model, review PR. Chỗ phải sửa lại output AI: (a) nháp bài toán CP1 dùng chữ "AI20K" trong khi đề cấm chữ "AI"; (b) AI mô tả học viên "vừa đi học vừa đi làm" — sai, phải sửa thành học viên của khoá; (c) lúc đầu AI không theo hướng gợi ý của track A, phải đọc lại `track-a-edtech.md` và chuyển sang A2; (d) hai thành viên chạy hai model khác nhau (Gemini và `gpt-5.4-mini`) nên số chi phí và tỉ lệ đạt không cùng gốc — phải chốt một model chính.

3. **Một câu thử trượt và mình học được gì:** B16 ("phòng C303 đang khám sức khỏe thì lab 3b sáng nay hc ở đâu ạ") — tin thật trên Discord, đúng nỗi đau nhóm chọn, nhưng lượt 2 vẫn trượt: trợ lý nêu đúng C204 mà không nói phòng đã đổi. Học được: code kiểm "phòng trong câu trả lời có trong thông báo" chỉ chặn được **sai**, không chặn được **thiếu** — câu đúng nhưng không nói rõ "đã đổi" vẫn làm học viên nghi ngờ. Muốn chặn phải có bước kiểm bằng code: thông báo được trích có `supersedes` thì câu trả lời phải nhắc thông báo cũ.

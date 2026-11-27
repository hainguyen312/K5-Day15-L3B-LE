# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

*Bản đầu CP2 — người viết: Vũ Đình Huy. Nhóm rà lại trước 19:30 Thứ Sáu 27/11.*

## Dataset 1 · Thông báo chính thức mẫu (`data/announcements.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `search_announcements` (và `get_thread`) · căn cứ của `expected` trong bộ câu thử |
| Từ đâu | **TB01–TB06:** viết lại từ tài liệu khoá có trong repo (`README.md`, `canvas.md`, `spec.md`, `eval/metric_spec.yaml`, `TEAMS.md`, `AGENTS.md`) — mỗi dòng có trường `source_ref` trỏ về file gốc. **TS01–TS07:** nhóm tự dựng (`synthetic`) |
| Xử lý những bước gì | Chọn các câu nói về hạn / nộp gì / nộp ở đâu → viết lại thành 1 thông báo / mốc · thêm trường `channel`, `posted_at`, `applies_to`, `supersedes`. Không có tên người, không có mã học viên. Không có script — viết tay |
| Số dòng / số đoạn | 13 thông báo: 6 viết lại + 7 synthetic |
| Phiên bản / ngày lấy | 27/11/2026, theo repo khung tại commit `6d20aec` |
| Nhãn | TB* = thật (viết lại) · TS* = `synthetic` (trường `label`) |
| Giới hạn | Chưa có thông báo Discord thật của khoá: TB* lấy từ tài liệu repo, `posted_at` và `channel` là giả định. TS* dùng tên "Lab mẫu M1–M4" để không nhầm với lab thật. Thiếu: thông báo dài nhiều ý, thông báo có ảnh / file đính kèm, thông báo bằng tiếng Anh, luồng trả lời (thread) |

**Data `synthetic` (TS01–TS07):** viết tay, không dùng model sinh, không có seed. Mỗi thông báo dựng để thử một chỗ khó ở `spec.md` §5:

| Thông báo | Thử chỗ khó gì | Câu thử |
|---|---|---|
| TS01 → TS02 | Thông báo cũ bị thay (đổi hạn + thêm yêu cầu) | B06 |
| TS03, TS04 | Hạn khác nhau theo lớp | B08 |
| TS05, TS06 | Hai thông báo mâu thuẫn, không cái nào thay cái nào | B07 |
| TS07 | Câu hỏi "nộp gì, ở đâu" bình thường | B04 |

Người kiểm: **TB01–TB06 (6/6)** Claude (trợ lý AI) đối chiếu với file gốc trong repo ngày 27/11/2026 (hạn, mục phải nộp, đường dẫn đều khớp); Huy cần rà lại. **TS01–TS07** nhóm tự dựng, **chưa có người ngoài nhóm rà** — chưa kiểm tay đủ 13/13. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Bộ câu thử (`eval/benchmark.csv`)

| | |
|---|---|
| Dùng để làm gì | Chạy `python run.py eval`, chấm theo `eval/metric_spec.yaml` |
| Từ đâu | Bản CP2: 15 câu nhóm tự viết (`tu_viet`). **Chưa có** câu từ người dùng thật |
| Xử lý những bước gì | Mỗi câu gắn với một thông báo (hoặc cố ý không có thông báo) và một lớp chỗ khó ở `spec.md` §5 (ghi trong cột `source`) |
| Số dòng / số đoạn | 15 câu: thuong 5 · kho 7 · tu_choi 3 (2 câu tấn công) |
| Phiên bản / ngày lấy | 27/11/2026 |
| Nhãn | `tu_viet` |
| Giới hạn | 0/15 câu từ người dùng / data thật — **chưa đạt ≥1/3**. Trước CP3 cần thêm câu lấy nguyên văn (đã bỏ tên) từ phỏng vấn (`evidence/interviews/P*.md`) và từ câu hỏi đếm được trên Discord (`evidence/data-mining.md`) để lên 20–30 câu, ≥1/3 `nguoi_dung` / `data_that` |

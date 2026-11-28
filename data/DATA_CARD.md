# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

*Bản đầu CP2 — người viết: Vũ Đình Huy. Nhóm rà lại trước 19:30 Thứ Sáu 27/11.*

## Dataset 1 · Thông báo chính thức mẫu (`data/announcements.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `search_announcements` (và `get_thread`) · căn cứ của `expected` trong bộ câu thử |
| Từ đâu | **TB01–TB06:** viết lại từ tài liệu khoá có trong repo (`README.md`, `canvas.md`, `spec.md`, `eval/metric_spec.yaml`, `TEAMS.md`, `AGENTS.md`) — mỗi dòng có trường `source_ref` trỏ về file gốc. **TS01–TS17:** nhóm tự dựng (`synthetic`) |
| Xử lý những bước gì | Chọn các câu nói về hạn / nộp gì / nộp ở đâu → viết lại thành 1 thông báo / mốc · thêm trường `channel`, `posted_at`, `applies_to`, `supersedes`. Không có tên người, không có mã học viên. Không có script — viết tay |
| Số dòng / số đoạn | 23 thông báo: 6 viết lại + 17 synthetic (TS08–TS17 thêm cho CP3: phòng / giờ học, thread, lịch Gate) |
| Phiên bản / ngày lấy | 27/11/2026, theo repo khung tại commit `6d20aec` |
| Nhãn | TB* = thật (viết lại) · TS* = `synthetic` (trường `label`) |
| Giới hạn | Chưa có thông báo Discord thật của khoá: TB* lấy từ tài liệu repo, `posted_at` và `channel` là giả định. TS* dùng tên "Lab mẫu M1–M4" để không nhầm với lab thật. Thiếu: thông báo dài nhiều ý, thông báo có ảnh / file đính kèm, thông báo bằng tiếng Anh, luồng trả lời (thread) |

**Data `synthetic` (TS01–TS17):** viết tay, không dùng model sinh, không có seed. Mỗi thông báo dựng để thử một chỗ khó ở `spec.md` §5:

| Thông báo | Thử chỗ khó gì | Câu thử |
|---|---|---|
| TS01 → TS02 | Thông báo cũ bị thay (đổi hạn + thêm yêu cầu) | B06 |
| TS03, TS04 | Hạn khác nhau theo lớp | B08 |
| TS05, TS06 | Hai thông báo mâu thuẫn, không cái nào thay cái nào | B07 |
| TS07 | Câu hỏi "nộp gì, ở đâu" bình thường | B04 |
| TS08 → TS09 | Phòng đổi sát giờ (thông báo đổi phòng có `supersedes`) | B16, B24 |
| TS10, TS11 | Hai lịch trùng giờ, không cái nào thay cái nào | B17 |
| *(không có)* | Không có thông báo lịch / daily standup / office hour / link online / vị trí phòng | B18, B21, B25, B26, B27 |
| TS12 | Câu đã được trả lời ở thread khác | B19 |
| TS13 → TS14 | Lịch Gate bị đổi (thông báo cũ bị thay) | B20 |
| TS15 | Phòng / giờ học thường | B22 |
| TS16, TS17 | Phòng / giờ khác nhau theo lớp, học viên không nói lớp | B23 |

Người kiểm: **TB01–TB06 (6/6)** Claude (trợ lý AI) đối chiếu với file gốc trong repo ngày 27/11/2026 (hạn, mục phải nộp, đường dẫn đều khớp); Huy cần rà lại. **TS01–TS17** nhóm tự dựng, **chưa có người ngoài nhóm rà** — chưa kiểm tay đủ 23/23. TS08–TS17 do Huy thêm ngày 28/11, chưa ai rà lại. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Bộ câu thử (`eval/benchmark.csv`)

| | |
|---|---|
| Dùng để làm gì | Chạy `python run.py eval`, chấm theo `eval/metric_spec.yaml` |
| Từ đâu | Bản CP2: 15 câu nhóm tự viết (`tu_viet`). CP3 thêm B16–B28: 11 câu `data_that` (trích ≤2 câu từ tin hỏi Discord `#chung`, bỏ tên; mã D010, D018, D019, D021, D025, D027 từ `evidence/data-mining.md` §4 và D002, D016, D024, D026, D031 do Nguyên gửi ở issue #9) + 2 câu `tu_viet` |
| Xử lý những bước gì | Mỗi câu gắn với một thông báo (hoặc cố ý không có thông báo) và một lớp chỗ khó ở `spec.md` §5 (ghi trong cột `source`) |
| Số dòng / số đoạn | 28 câu: thuong 7 · kho 17 · tu_choi 4 (2 câu tấn công) |
| Phiên bản / ngày lấy | CP2 27/11/2026 · thêm B16–B28 ngày 28/11/2026 |
| Nhãn | `tu_viet` · `data_that` |
| Giới hạn | **11/28 câu `data_that` (39%), đạt ≥1/3**; chưa có câu `nguoi_dung` (lời P3, T1 không phải câu hỏi nguyên văn). Câu `data_that` chỉ có câu hỏi; `expected` do nhóm viết dựa trên thông báo mẫu `synthetic`, không phải câu trả lời thật của TA. B20 dùng câu thật D019 nhưng TS13/TS14 dựng lại tình huống "lịch bị dời"; trên Discord thật admin trả lời học viên là xem nhầm — khi demo phải nói rõ là tình huống dựng lại. Các tin D0xx chỉ thuộc kênh `#chung`, 16–26/11 |

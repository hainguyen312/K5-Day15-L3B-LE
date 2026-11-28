# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu —
  - `chi_nghe_tren_lop` 60% · 1 phiên / tháng · 1 lượt / phiên — P1, P2: 0 lần phải tìm lại trong tháng qua
  - `hoi_khi_thong_tin_doi` 30% · 4 phiên / tháng · 2 lượt / phiên — P3: hỏi lại 1 lần gần nhất + 2–3 lần những ngày đầu
  - `hoi_don_khi_doi_phong` 10% · 8 phiên / tháng · 1 lượt / phiên — Discord: 3 lần đổi phòng / giờ sát giờ trong 11 ngày, D025 có thêm 3 tin "+1" (`evidence/data-mining.md`)
  - Nguồn: `evidence/interviews/P1.md`–`P3.md`, `evidence/data-mining.md` §3. **Tỉ lệ 60 / 30 / 10 và số phiên / tháng là *(tự ước tính, n = 3)*.**
- **Số người dùng thật** 3 kịch bản: thấp **436** · cơ sở **700** · cao **1.000**. Nguồn: thấp — 436 học viên có hoạt động trên trang pre-class (`data/preclass/README.md` của repo đề) · cơ sở — lớp L3 hơn 700 học viên (`tracks/track-a-edtech.md`, mục A5) · cao — khoá K5 hơn 1.000 học viên (`tracks/track-a-edtech.md`, Bối cảnh).
- **Giá** 4 mức model (USD / 1M token vào · ra, `further-reading/model-prices.md` của repo đề, BTC xem 25/11/2026): `gpt-5.4-mini` 0,75 · 4,50 (https://developers.openai.com/api/docs/pricing) · `gemini-3.1-flash-lite` 0,25 · 1,50 · `gemini-3.5-flash-lite` 0,30 · 2,50 · `gemini-4-hydrogen` 1,50 · 7,50 (https://ai.google.dev/gemini-api/docs/pricing)
- **Tỉ lệ đạt** dùng để tính: **24/28 (86%)** — lượt `run-2@20261128-100129` (lượt 2, cùng model `gpt-5.4-mini`)
- Đo token trên model **`gpt-5.4-mini`**, tính giá model `gpt-5.4-mini`, `gemini-3.1-flash-lite`, `gemini-3.5-flash-lite` và `gemini-4-hydrogen` (model khác bộ tách token nên số token thật có thể lệch).

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-2.csv` · run ID `simulate-2@20261128-124022` · **50 phiên** · seed 42 · phiên lỗi 0/50 · trace `traces/simulate-2.jsonl`

> `cost/simulate-1.csv` (`simulate-1@20261128-123900`) bị **mất mạng giữa chừng: 14/50 phiên lỗi** `URLError getaddrinfo failed` từ phiên S035 → chạy lại cùng seed thành `simulate-2`. Giữ `simulate-1` làm lịch sử, không dùng số của nó.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| chi_nghe_tren_lop | 32 | 1 | 917 | 33 | 0.9 | 4.4 |
| hoi_khi_thong_tin_doi | 15 | 2 | 2002 | 77 | 1.9 | 10.4 |
| hoi_don_khi_doi_phong | 3 | 1 | 1118 | 33 | 1.0 | 5.0 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (436) | / tháng — cơ sở (700) | / tháng — cao (1.000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| **gpt-5.4-mini** (model chính) | $0.0011 | **$0.0013** | $1.53 | **$2.46** | $3.51 | $0.0035 |
| gemini-3.1-flash-lite | $0.00038 | $0.00045 | $0.51 | $0.82 | $1.17 | $0.0012 |
| gemini-3.5-flash-lite | $0.00049 | $0.00057 | $0.66 | $1.05 | $1.50 | $0.0015 |
| gemini-4-hydrogen | $0.0022 | $0.0026 | $2.97 | $4.77 | $6.81 | $0.0068 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (86%) — **không coi như đạt 100%**. Bảng chép từ `cost/simulate-2-summary.md` (số / tháng làm tròn 2 chữ số).

- **Chi phí / task thành công ở kịch bản cơ sở: $0.0013 (model `gpt-5.4-mini`)** — đo trên `gpt-5.4-mini`, tính giá `gpt-5.4-mini`.
- Một phiên ~1 lần gọi model + 4–5 lần gọi công cụ chỉ đọc (workflow cố định, model chỉ quyết 1 lần mỗi lượt). 4/50 phiên không gọi model (câu "Lab M5 nộp gì" — code trả lời "không có thông báo" trước khi gọi model) nên chi phí bằng 0.
- So với bản thử CP3 (10 phiên, chưa có persona `hoi_don_khi_doi_phong`): $2.86 → $2.46 / tháng (cơ sở) — cùng bậc, khác do mẫu phiên.

## 3. So với impact

- Impact / tháng (`spec.md` §2): ~33 câu hỏi logistics công khai × 10–30 phút ≈ **5,5–16,5 giờ chờ / tháng** chỉ riêng kênh `#chung` *(tự ước tính)*, chưa tính điểm bị trừ do nộp sai / đến nhầm phòng.
- Chi phí / người / tháng (cơ sở, model `gpt-5.4-mini`): **$0.0035** · cả lớp 700 người: **$2.46 / tháng**.
- **Kết luận một dòng — đáng làm không:** **Đáng** — $2.46 / tháng cho cả lớp ≈ dưới $0.45 cho mỗi giờ chờ tiết kiệm được (theo cận thấp 5,5 giờ); chi phí model không phải điểm nghẽn, điểm nghẽn là **giờ TA duyệt nháp** và độ đúng của bộ thông báo khi nối Discord thật.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- **Model rẻ hơn:** chuyển `gemini-3.1-flash-lite` giảm ~3 lần ($2.46 → $0.82 / tháng) nhưng **chưa có tỉ lệ đạt đo trên Gemini** (lượt Gemini `run-1@20261128-094905` chưa chấm) — không đổi model chỉ vì giá.
- **Chi phí ngoài model (chưa đo):** giờ công TA duyệt nháp `escalate` — số nháp / tháng = số câu không có thông báo / mâu thuẫn; cần đo ở bước pilot. Hosting: bot chạy 1 tiến trình nhỏ, *(tự ước tính, chưa tính)*.
- **Quy mô:** chi phí tăng tuyến tính theo người dùng; ở cả khoá 1.000 người vẫn $3.51 / tháng.

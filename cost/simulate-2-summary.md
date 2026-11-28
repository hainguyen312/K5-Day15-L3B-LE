# Tóm tắt mô phỏng simulate-2@20261128-124022

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| chi_nghe_tren_lop | 32 | 1 | 917 | 33 | 0.9 | 4.4 |
| hoi_khi_thong_tin_doi | 15 | 2 | 2002 | 77 | 1.9 | 10.4 |
| hoi_don_khi_doi_phong | 3 | 1 | 1118 | 33 | 1.0 | 5.0 |

Tỉ lệ đạt dùng để tính: 24/28 (86%) — lượt run-2@20261128-100129

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-2.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (436 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0011 | $0.0013 | $0.0010 | $1.53 | $2.46 | $3.51 | $0.0035 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00038 | $0.00045 | $0.00034 | $0.5104 | $0.8194 | $1.17 | $0.0012 |
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00049 | $0.00057 | $0.00044 | $0.6550 | $1.05 | $1.50 | $0.0015 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0022 | $0.0026 | $0.0020 | $2.97 | $4.77 | $6.81 | $0.0068 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.3) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.

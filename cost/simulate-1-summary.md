# Tóm tắt mô phỏng simulate-1@20261128-123900

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| chi_nghe_tren_lop | 26 | 1 | 877 | 33 | 0.8 | 4.2 |
| hoi_khi_thong_tin_doi | 8 | 2 | 2023 | 72 | 1.9 | 10.5 |
| hoi_don_khi_doi_phong | 2 | 1 | 995 | 26 | 1.0 | 4.5 |

Tỉ lệ đạt dùng để tính: 24/28 (86%) — lượt run-2@20261128-100129

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-2.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (436 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0010 | $0.0012 | $0.00099 | $1.47 | $2.37 | $3.38 | $0.0034 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00035 | $0.00040 | $0.00033 | $0.4915 | $0.7891 | $1.13 | $0.0011 |
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00044 | $0.00052 | $0.00042 | $0.6284 | $1.01 | $1.44 | $0.0014 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0020 | $0.0024 | $0.0019 | $2.87 | $4.60 | $6.57 | $0.0066 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 14/50.

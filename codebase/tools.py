"""Công cụ của trợ lý Discord A2 — NHÓM VIẾT (Quân). Thiết kế ở spec.md §4.

Dữ liệu: data/announcements.json (mô tả ở data/DATA_CARD.md).
Format do Huy chốt (data/DATA_CARD.md): id (TB01, TS01…) · label · channel · author_role · posted_at ·
applies_to (tat_ca / L3A / L3B) · title · text · supersedes (id thông báo bị nó thay, hoặc null) · source_ref.
Trường link (tuỳ chọn): có thì trợ lý trả link, chưa có thì trả kênh + giờ đăng.

| Công cụ               | Input              | Output                                         | Tác động ra ngoài? |
|-----------------------|--------------------|------------------------------------------------|--------------------|
| search_announcements  | câu hỏi (str)      | ≤5 thông báo khớp nhất                         | Không              |
| get_thread            | mã thông báo (str) | chuỗi thông báo thay thế nhau + mã bản mới nhất | Không              |
| escalate              | câu hỏi, lý do     | BẢN NHÁP tin tag TA, chờ người duyệt           | Có → chỉ tạo nháp  |
"""
import json
import os
import re
import unicodedata

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.environ.get("ANNOUNCEMENTS_PATH") or os.path.join(ROOT, "data", "announcements.json")

# Từ quá phổ biến trong câu hỏi logistics, không giúp phân biệt thông báo nào
STOPWORDS = {
    "la", "khi", "nao", "gi", "o", "dau", "cho", "cua", "va", "thi", "co", "khong", "a", "nhe",
    "em", "minh", "anh", "chi", "ban", "oi", "voi", "the", "nay", "do", "may", "bao", "nhieu",
    "duoc", "can", "phai", "vay", "sao", "ai", "mot", "nhung", "cac", "trong", "tren",
}

# Mã định danh: "lab 12", "Lab mẫu M4", "cp2", "checkpoint 3" → ("lab", "12"), ("lab", "m4"), ("cp", "2")
_IDENT = re.compile(r"\b(lab|cp|checkpoint)\s*(?:mau\s*)?[-#]?\s*([a-z]?\d+)\b")


def _norm(text: str) -> str:
    """Chữ thường, bỏ dấu tiếng Việt (đ → d) để so khớp không phụ thuộc gõ dấu."""
    text = unicodedata.normalize("NFD", (text or "").lower().replace("đ", "d"))
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _identifiers(text: str) -> set:
    out = set()
    for kind, num in _IDENT.findall(_norm(text)):
        out.add(("cp" if kind == "checkpoint" else kind, num))
    return out


def _words(text: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", _norm(text)) if w not in STOPWORDS and len(w) > 1}


def _load() -> list:
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data["announcements"] if isinstance(data, dict) else data


@tool
def search_announcements(query: str, top_k: int = 5) -> list:
    """search_announcements — tra thông báo chính thức theo câu hỏi.
    Input: câu hỏi của học viên (str), top_k (int, mặc định 5).
    Output: danh sách ≤top_k thông báo (nguyên các trường trong data), khớp nhất trước.
            Câu hỏi có mã (vd "lab 12", "CP2") thì chỉ trả thông báo nhắc đúng mã đó.
    Tác động ra ngoài: Không (chỉ đọc data/announcements.json)."""
    q_ids = _identifiers(query)
    q_words = _words(query)
    scored = []
    for a in _load():
        body = a["title"] + " " + a["text"]
        a_ids = _identifiers(body)
        if q_ids and not (q_ids & a_ids):
            continue  # hỏi lab 12 thì không trả thông báo lab 13
        score = 3 * len(q_ids & a_ids) + len(q_words & _words(body))
        if score > 0:
            scored.append((score, a.get("posted_at", ""), a))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return [a for _, _, a in scored[:top_k]]


@tool
def get_thread(announcement_id: str) -> dict:
    """get_thread — lấy chuỗi thông báo liên quan (bản gốc, các bản đính chính / thay thế).
    Input: mã thông báo (str, vd "TB01").
    Output: {"chain": [thông báo, cũ → mới], "latest": mã bản mới nhất còn hiệu lực}
            hoặc {"chain": [], "latest": None} nếu không có mã đó.
    Tác động ra ngoài: Không."""
    items = {a["id"]: a for a in _load()}
    if announcement_id not in items:
        return {"chain": [], "latest": None}
    replaced_by = {a["supersedes"]: a["id"] for a in items.values() if a.get("supersedes")}
    # lùi về bản gốc
    first, seen = announcement_id, set()
    while items[first].get("supersedes") in items and first not in seen:
        seen.add(first)
        first = items[first]["supersedes"]
    # tiến tới bản mới nhất
    chain, cur, seen = [items[first]], first, {first}
    while cur in replaced_by and replaced_by[cur] not in seen:
        cur = replaced_by[cur]
        seen.add(cur)
        chain.append(items[cur])
    return {"chain": chain, "latest": cur}


@tool
def escalate(question: str, reason: str) -> dict:
    """escalate — soạn tin nhắn tag TA khi trợ lý không đủ căn cứ để trả lời.
    Input: câu hỏi gốc (str), lý do chuyển (str, vd "không có thông báo", "hai thông báo mâu thuẫn").
    Output: {"status": "draft", "to": "@TA", "message": str} — CHỈ LÀ BẢN NHÁP.
    Tác động ra ngoài: CÓ nếu gửi → công cụ này KHÔNG gửi; TA / người duyệt bấm gửi."""
    message = ("@TA nhờ xác nhận giúp câu hỏi của học viên: \"%s\"\n"
               "Lý do trợ lý chuyển: %s." % (question.strip(), reason))
    return {"status": "draft", "to": "@TA", "message": message}

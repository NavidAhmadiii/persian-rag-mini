from config import CHUNK_OVERLAP_WORDS, CHUNK_SIZE_WORDS


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE_WORDS, overlap: int = CHUNK_OVERLAP_WORDS) -> list[str]:

    words = text.split()
    if len(words) <= chunk_size:
        return [text]

    chunks = []
    step = chunk_size - overlap
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))

        if end >= len(words):
            break
        start += step

    return chunks


def chunk_documents(docs: list[dict]) -> list[dict]:
    all_chunks = []
    for doc in docs:
        for j, ch in enumerate(chunk_text(doc["text"])):
            all_chunks.append({
                "id": f"{doc['id']}#{j}",
                "text": ch,
                "doc_id": doc["id"],
            })
    return all_chunks

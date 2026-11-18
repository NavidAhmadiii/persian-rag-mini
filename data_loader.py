import ir_datasets
from config import DATASET_NAME, MAX_DOCS


def load_documents():
    dataset = ir_datasets.load(DATASET_NAME)
    docs = []
    for i, doc in enumerate(dataset.docs_iter()):
        if i >= MAX_DOCS:
            break
        text = (doc.text or "").strip()

        if len(text) < 20:
            continue

        docs.append({
            "id": doc.doc_id,
            "text": text
        })تع
    return docs

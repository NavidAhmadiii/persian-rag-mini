DATASET_NAME = "neumarco/fa"
MAX_DOCS = 5000

CHUNK_SIZE_WORDS = 300
CHUNK_OVERLAP_WORDS = 50

# --- Embedding ---
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
EMBEDDING_BATCH_SIZE = 64

# --- Vector Store ---
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "neumarco_fa_chunks"
TOP_K = 5

# --- Generation ---
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:3b"

"""
Enterprise RAG Knowledge Assistant
----------------------------------
Central configuration file.

Change application settings here instead of modifying
multiple files throughout the project.
"""

# ===============================
# Document Settings
# ===============================

DOCUMENTS_PATH = "data/documents"

# ===============================
# Vector Database
# ===============================

VECTOR_STORE_PATH = "vector_store/faiss_index"

# ===============================
# Embedding Model
# ===============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ===============================
# LLM Configuration
# ===============================

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.2

MAX_OUTPUT_TOKENS = 1024

# ===============================
# Chunking
# ===============================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# ===============================
# Retrieval
# ===============================

TOP_K = 3

# ===============================
# UI
# ===============================

APP_TITLE = "Enterprise RAG Knowledge Assistant"

PAGE_ICON = "🤖"
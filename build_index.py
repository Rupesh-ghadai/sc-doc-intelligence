import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_document(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

# 1. Load and chunk the document
document_text = load_document("contract.txt")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = splitter.split_text(document_text)
print(f"Created {len(chunks)} chunks")

# 2. Set up ChromaDB with a local embedding model
chroma_client = chromadb.PersistentClient(path="./chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 3. Create (or reset) a collection
collection_name = "sc_documents"
try:
    chroma_client.delete_collection(collection_name)
except Exception:
    pass

collection = chroma_client.create_collection(
    name=collection_name,
    embedding_function=embedding_fn
)

# 4. Add chunks with metadata
ids = [f"chunk_{i}" for i in range(len(chunks))]
metadatas = [{"source": "contract.txt", "chunk_index": i} for i in range(len(chunks))]

collection.add(
    documents=chunks,
    ids=ids,
    metadatas=metadatas
)

print(f"Indexed {len(chunks)} chunks into ChromaDB at ./chroma_db")
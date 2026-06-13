import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.PersistentClient(path="./chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = chroma_client.get_collection(
    name="sc_documents",
    embedding_function=embedding_fn
)

def retrieve(question, top_k=3):
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    return results

if __name__ == "__main__":
    question = "How much do I get penalized if delivery performance drops?"

    results = retrieve(question)

    print(f"Question: {question}\n")
    for i, (doc, distance) in enumerate(zip(results["documents"][0], results["distances"][0])):
        print(f"--- Match {i+1} (distance: {distance:.4f}) ---")
        print(doc)
        print()
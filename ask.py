import sys
import chromadb
from chromadb.utils import embedding_functions
from anthropic import Anthropic

def load_api_key():
    with open(".env", encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY"):
                return line.split("=", 1)[1].strip()

def retrieve_chunks(question, top_k=3):
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    collection = chroma_client.get_collection(
        name="sc_documents",
        embedding_function=embedding_fn
    )
    results = collection.query(query_texts=[question], n_results=top_k)
    return results["documents"][0], results["metadatas"][0]

def main():
    if len(sys.argv) < 2:
        print('Usage: python ask.py "<question>"')
        sys.exit(1)

    question = sys.argv[1]

    chunks, metadatas = retrieve_chunks(question, top_k=3)

    context = "\n\n---\n\n".join(chunks)

    client = Anthropic(api_key=load_api_key())

    prompt = f"""You are a supply chain document analyst. Answer the question
using ONLY the information in the context below. If the answer is not
present in the context, say clearly: "This document does not contain
information about that."

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(response.content[0].text)
    print("\n--- Retrieved chunks used ---")
    for i, chunk in enumerate(chunks):
        print(f"\n[{i+1}] {chunk[:100]}...")

if __name__ == "__main__":
    main()
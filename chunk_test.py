from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_document(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

document_text = load_document("contract.txt")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(document_text)

print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i} ({len(chunk)} chars) ---")
    print(chunk)
    print()
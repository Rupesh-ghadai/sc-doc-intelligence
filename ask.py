import sys
from anthropic import Anthropic

def load_api_key():
    with open(".env", encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY"):
                return line.split("=", 1)[1].strip()

def load_document(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) < 3:
        print("Usage: python ask.py <document_path> \"<question>\"")
        sys.exit(1)

    doc_path = sys.argv[1]
    question = sys.argv[2]

    document_text = load_document(doc_path)

    client = Anthropic(api_key=load_api_key())

    prompt = f"""You are a supply chain document analyst. Answer the question
using ONLY the information in the document below. If the answer is not
present in the document, say clearly: "This document does not contain
information about that."

When you answer, cite the relevant section number from the document.

DOCUMENT:
{document_text}

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

if __name__ == "__main__":
    main()
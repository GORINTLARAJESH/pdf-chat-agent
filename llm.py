from pdf_processor import extract_text
from chunker import split_text
from embeddings import create_embeddings
from vector_store import create_index
from retriever import retrieve

from ollama import chat


def generate_answer(context, question):
    prompt = f"""
You are a helpful PDF assistant.

Answer ONLY using the given context.

If the answer is not present in the context, say:
"I couldn't find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = chat(
        model="gemma3:1b",   # or llama3.2 if you installed it
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    # Step 1: Read PDF
    text = extract_text("uploads/sample.pdf")

    # Step 2: Split into chunks
    chunks = split_text(text)

    # Step 3: Generate embeddings
    embeddings = create_embeddings(chunks)

    # Step 4: Store in FAISS
    index = create_index(embeddings)

    # Step 5: Ask a question
    question = input("Ask a question: ")

    # Step 6: Retrieve relevant chunks
    retrieved_chunks = retrieve(question, index, chunks)

    # Step 7: Combine chunks into context
    context = "\n\n".join(retrieved_chunks)

    # Step 8: Generate answer
    answer = generate_answer(context, question)

    print("\nAnswer:\n")
    print(answer)
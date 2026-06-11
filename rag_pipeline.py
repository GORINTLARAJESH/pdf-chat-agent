from pdf_processor import extract_text
from chunker import split_text
from embeddings import create_embeddings
from vector_store import create_index
from retriever import retrieve
from llm import generate_answer


def answer_question(pdf_path, question):
    # Extract text
    text = extract_text(pdf_path)

    if not text.strip():
        raise ValueError("No text found in PDF. The PDF may be scanned or image-based.")

    # Split into chunks
    chunks = split_text(text)
    if len(chunks) == 0:
        raise ValueError("No chunks created. Check the chunking logic.")

    # Generate embeddings
    embeddings = create_embeddings(chunks)
    print("Text Length:", len(text))

    print("Chunks:", len(chunks))

    print("Embeddings Shape:", embeddings.shape)

    print(type(embeddings))

    # Create FAISS index
    index = create_index(embeddings)

    # Retrieve relevant chunks
    retrieved_chunks = retrieve(question, index, chunks)

    # Convert list to string
    context = "\n\n".join(retrieved_chunks)

    # Generate answer
    answer = generate_answer(context, question)
    text = extract_text(pdf_path)
    print("TEXT LENGTH:", len(text))

    chunks = split_text(text)
    print("NUMBER OF CHUNKS:", len(chunks))

    embeddings = create_embeddings(chunks)
    print("EMBEDDINGS SHAPE:", embeddings.shape)

    return answer
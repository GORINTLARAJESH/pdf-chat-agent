import faiss
import numpy as np

def create_index(embeddings):

    embeddings = np.array(embeddings, dtype=np.float32)

    if embeddings.ndim != 2:
        raise ValueError(
            f"Expected 2D embeddings, got {embeddings.shape}"
        )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


if __name__ == "__main__":

    from pdf_processor import extract_text
    from chunker import split_text
    from embeddings import create_embeddings

    # Extract text
    text = extract_text("uploads/sample.pdf")

    # Create chunks
    chunks = split_text(text)

    # Generate embeddings
    embeddings = create_embeddings(chunks)

    # Build index
    index = create_index(embeddings)

    print("Total vectors stored:", index.ntotal)
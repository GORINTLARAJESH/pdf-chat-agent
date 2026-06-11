import numpy as np

from embeddings import create_embeddings


def retrieve(query, index, chunks, top_k=3):
    """
    Retrieve the most relevant chunks for a query.
    """

    # Convert question into embedding
    query_embedding = create_embeddings([query])

    # Convert to float32
    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    # Get matching chunks
    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks
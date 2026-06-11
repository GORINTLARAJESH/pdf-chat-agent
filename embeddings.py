from sentence_transformers import SentenceTransformer

from pdf_processor import extract_text
from chunker import split_text

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Convert text chunks into embeddings.
    """
    embeddings = model.encode(chunks)
    return embeddings


# Test
if __name__ == "__main__":

    # Step 1: Extract text from PDF
    text = extract_text("uploads/sample.pdf")

    # Step 2: Split text into chunks
    chunks = split_text(text)

    # Step 3: Generate embeddings
    embeddings = create_embeddings(chunks)

    # Step 4: Print results
    print("Total Chunks:", len(chunks))
    print("Total Embeddings:", len(embeddings))
    print("Dimensions:", len(embeddings[0]))

    # Optional: Print first 10 values of first embedding
    print("\nFirst 10 values of first embedding:")
    print(embeddings[0][:10])
def split_text(text, chunk_size=500):
    """
    Splits text into fixed-size chunks.

    Args:
        text (str): Input text.
        chunk_size (int): Number of characters per chunk.

    Returns:
        list: List of text chunks.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


# Test
if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is transforming industries.
    Machine Learning is a subset of AI.
    Deep Learning uses neural networks.
    Natural Language Processing enables machines to understand text.
    """ * 20

    chunks = split_text(sample_text)

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n------ Chunk {i} ------\n")
        print(chunk)
import fitz  # PyMuPDF


def extract_text(pdf_path):
    """
    Extracts all text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Complete text extracted from the PDF.
    """

    # Open the PDF
    document = fitz.open(pdf_path)

    # Store text from all pages
    text = ""

    # Loop through every page
    for page in document:
        text += page.get_text()

    # Close the document
    document.close()

    return text


# Test the function
if __name__ == "__main__":

    pdf_path = "uploads/sample.pdf"

    extracted_text = extract_text(pdf_path)

    print("=" * 50)
    print("TEXT LENGTH:", len(extracted_text))
    print("=" * 50)

    if extracted_text.strip():
        print(extracted_text[:1000])
    else:
        print("❌ No text extracted from PDF")
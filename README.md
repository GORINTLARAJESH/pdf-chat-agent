# 🤖 PDF Chat Agent

An AI-powered PDF Question Answering application built using **Retrieval-Augmented Generation (RAG)**, **FAISS**, **Sentence Transformers**, **Ollama**, and **Streamlit**. Upload a PDF, ask questions in natural language, and receive context-aware answers generated from the document.

---

## 🚀 Features

* 📄 Upload PDF documents
* 💬 Chat with your PDFs
* 🧠 Semantic Search using Embeddings
* 🔍 Fast Vector Search with FAISS
* 🤖 Local LLM support using Ollama (Gemma)
* ⚡ Retrieval-Augmented Generation (RAG)
* 🎨 Interactive Streamlit UI
* 🔒 Runs completely on your local machine

---

## 🏗️ Project Structure

```text
pdf-chat-agent/
│
├── uploads/
│
├── pdf_processor.py
├── chunker.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── llm.py
├── rag_pipeline.py
├── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

* Python
* Streamlit
* PyMuPDF
* Sentence Transformers
* FAISS
* Ollama
* Gemma
* NumPy

---

## 🔄 Working Flow

```text
                PDF
                 │
                 ▼
        Text Extraction
                 │
                 ▼
            Text Chunking
                 │
                 ▼
        Generate Embeddings
                 │
                 ▼
        Store in FAISS Index

────────────────────────────────────

          User Question
                 │
                 ▼
      Generate Query Embedding
                 │
                 ▼
      Semantic Search (FAISS)
                 │
                 ▼
      Retrieve Relevant Chunks
                 │
                 ▼
      Build Context + Prompt
                 │
                 ▼
      Ollama (Gemma Model)
                 │
                 ▼
          Final AI Response
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/GORINTLARAJESH/pdf-chat-agent.git

cd pdf-chat-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Gemma model:

```bash
ollama pull gemma3:1b
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

Then open:

```
http://localhost:8501
```

---

## 💡 Example

**User:**

> What is the role of a Data Analyst?

**Assistant:**

> A Data Analyst collects, processes, and analyzes data to identify trends, generate insights, and support data-driven decision-making within an organization.

---

## 📚 Core Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* FAISS Vector Database
* Similarity Search
* Chunking
* Local LLM Inference
* Prompt Engineering

---

## 🔮 Future Improvements

* OCR Support for Scanned PDFs
* Multi-PDF Chat
* Chat History Persistence
* Source Citations
* Page Number References
* Streaming Responses
* Multiple LLM Support
* Hybrid Search (BM25 + Vector Search)
* Authentication
* Cloud Deployment

## 👨‍💻 Author

**Gorintla Rajesh**

If you found this project useful, consider giving it a ⭐ on GitHub.

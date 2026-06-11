import os
import streamlit as st

from rag_pipeline import answer_question

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="PDF Chat Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main App */
.stApp{
    background:#0B1120;
}

/* Main Container */
.block-container{
    max-width:1350px;
    padding-top:2rem;
    padding-bottom:1rem;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* Title */
.main-title{
    font-size:64px;
    font-weight:800;
    text-align:center;
    color:white;
    margin-bottom:0px;
    line-height:1.2;
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:#9CA3AF;
    font-size:22px;
    margin-bottom:30px;
}

/* Cards */
.custom-card{
    background:#172554;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

/* Footer */
.footer{
    text-align:center;
    color:#9CA3AF;
    padding:20px;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:48px;
}

/* Chat */
[data-testid="stChatMessage"]{
    border-radius:12px;
}

/* File Uploader */
[data-testid="stFileUploader"]{
    border:2px dashed #2563EB;
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 PDF Chat Agent")

    st.success("🟢 Ollama Connected")

    st.info("LLM : Gemma 3")

    st.info("Vector DB : FAISS")

    st.info("Embedding : all-MiniLM-L6-v2")

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.session_state.pdf_path = save_path
        st.session_state.pdf_name = uploaded_file.name

        st.success("✅ PDF Uploaded")

        st.write(uploaded_file.name)

        st.caption(
            f"Size : {round(uploaded_file.size/1024,2)} KB"
        )

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("""
<div class="main-title">
🤖 PDF Chat Agent
</div>

<div class="sub-title">
Upload • Search • Retrieve • Chat
</div>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------

# --------------------------------------------------
# Current PDF
# --------------------------------------------------

if st.session_state.pdf_name:

    st.markdown(f"""
    <div class="custom-card">

    ### 📄 Current Document

    **{st.session_state.pdf_name}**

    </div>
    """, unsafe_allow_html=True)
else:

    st.info("Upload a PDF from the sidebar.")

# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask anything about your PDF..."
)

# --------------------------------------------------
# Generate Answer
# --------------------------------------------------

if question:

    if st.session_state.pdf_path is None:

        st.warning("Please upload a PDF first.")

    else:

        # User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user", avatar="👤"):

            st.markdown(question)

        # Assistant

        with st.chat_message("assistant", avatar="🤖"):

            with st.spinner(
                "🧠 Creating embeddings...\n\n🔍 Searching FAISS...\n\n🤖 Generating answer..."
            ):

                try:

                    answer = answer_question(
                        st.session_state.pdf_path,
                        question
                    )

                except Exception as e:

                    answer = f"❌ Error:\n\n{str(e)}"

            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.markdown(
    """
<div class='footer'>
Built with ❤️ using Streamlit • FAISS • Sentence Transformers • Ollama
</div>
""",
    unsafe_allow_html=True
)

#Welcome Card
# --------------------------------------------------

st.markdown("""
<div class="custom-card">

### 👋 Welcome

- 📄 Upload your PDF
- 🔍 Semantic Search using FAISS
- 🧠 MiniLM Embeddings
- 🤖 Gemma 3 via Ollama
- 💬 Ask unlimited questions

</div>
""", unsafe_allow_html=True)
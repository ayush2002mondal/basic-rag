# 🤖 Your Friendly HR — AI-Powered HR Policy Assistant

An AI-powered HR Policy Assistant built using **Retrieval-Augmented Generation (RAG)** that helps employees get quick, accurate answers to questions about company HR policies.

Instead of manually searching through lengthy policy documents, users can simply ask questions in natural language and receive context-aware answers grounded in the provided HR documentation.

<p align="center">

  <a href="https://yourfriendlyhr.streamlit.app/">
    <strong>🚀 Try the Live Application</strong>
  </a>

</p>

---

## 🌐 Live Demo

**[Your Friendly HR — Try it here](https://yourfriendlyhr.streamlit.app/)**

---

## 📌 About the Project

Your Friendly HR is a conversational AI assistant designed to simplify access to company HR policies.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from HR documents and provide meaningful responses using a Large Language Model (LLM).

The project demonstrates the fundamentals of building a RAG application, from document ingestion and vector embeddings to retrieval, LLM integration, and deployment using Streamlit.

### ✨ Key Features

- 💬 **Conversational Interface:** Ask HR-related questions using natural language.
- 📚 **Document-Based Responses:** Answers are grounded in the provided HR policy document.
- 🔍 **Semantic Search:** Retrieves relevant information using vector similarity.
- 🧠 **Retrieval-Augmented Generation:** Combines retrieved context with an LLM to generate responses.
- ⚡ **Persistent Vector Storage:** Stores the FAISS index locally to avoid unnecessary reprocessing.
- 🖥️ **Interactive UI:** Simple and intuitive interface built with Streamlit.
- ☁️ **Live Deployment:** Accessible through the deployed Streamlit application.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline and LLM orchestration |
| Groq | Large Language Model inference |
| Jina AI Embeddings | Text embedding generation |
| FAISS | Vector storage and similarity search |
| Streamlit | Interactive web application |
| UV | Python package and environment management |
| Jupyter Notebook | Experimentation and prototyping |
| Git & GitHub | Version control |

---

## 🧠 How It Works

The application follows a traditional RAG architecture consisting of two major pipelines.

### 1. Data Ingestion Pipeline

The HR policy document is processed and converted into searchable vector representations.

```text
HR Policy Document
        |
        v
  Document Loading
        |
        v
   Text Splitting
        |
        v
  Text Embeddings
    (Jina AI)
        |
        v
  FAISS Vector Store
        |
        v
 Persistent Local Index
```

### 2. Data Retrieval & Generation Pipeline

When a user asks a question, the system retrieves relevant chunks from the vector store and passes them to the LLM.

```text
   User Question
        |
        v
  Semantic Retrieval
        |
        v
  Relevant HR Context
        |
        v
  System Prompt
        |
        v
   Groq LLM
        |
        v
  Generated Response
        |
        v
  Streamlit Interface
```

This approach helps the assistant generate responses based on the available HR documentation rather than relying entirely on the LLM's general knowledge.

---

## 🏗️ Project Structure

```text
basic-rag/
│
├── data/
│   └── hr_policy.txt
│
├── hr_assistant/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── ...
│
├── app.py
├── main.py
├── rag.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

**Core components:**

- `config.py` — Centralized configuration, model settings, API keys, and paths.
- `document_loader.py` — Loads the HR policy document.
- `splitter.py` — Splits documents into smaller overlapping chunks.
- `embeddings.py` — Initializes the embedding model.
- `vectorstore.py` — Builds, saves, and loads the FAISS vector store.
- `main.py` — Coordinates the RAG pipeline.
- `app.py` — Streamlit user interface.
- `rag.ipynb` — Notebook for experimentation and understanding the RAG workflow.

---

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/ayush2002mondal/basic-rag.git

cd basic-rag
```

### 2. Create a Virtual Environment

Install UV:

```bash
pip install uv
```

Create a virtual environment:

```bash
uv venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
```

You can obtain API keys from:

- [Groq Console](https://console.groq.com/)
- [Jina AI](https://jina.ai/)

**Important:** Never commit your `.env` file or expose API keys publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the HR assistant.

---

## 💡 Example Use Cases

The assistant can be used to ask questions such as:

- What is the company's leave policy?
- How many days of leave are employees entitled to?
- What is the work-from-home policy?
- What is the probation period?
- What is the notice period?
- What is the reimbursement policy?

The responses depend on the information available in the HR policy document.

---

## 🎯 Learning Outcomes

Through this project, I explored and implemented:

- Fundamentals of Retrieval-Augmented Generation.
- Document loading and text chunking.
- Semantic embeddings and vector databases.
- Similarity-based document retrieval.
- LLM integration using LangChain and Groq.
- Modular programming and reusable Python components.
- Persistent vector storage using FAISS.
- Building interactive AI applications with Streamlit.
- Deploying an AI-powered application.

---

## 🚀 Future Improvements

- Support for multiple PDF and document formats.
- Improved retrieval using reranking.
- Chat history and conversational memory.
- More advanced retrieval strategies.
- Better source citations for generated answers.
- Integration with cloud-based vector databases.

---


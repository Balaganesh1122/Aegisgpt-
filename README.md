# 🛡️ AegisGPT

> **Enterprise AI-Powered Document Intelligence Platform**
>
> Upload documents, perform semantic search, and chat with your PDFs using **Retrieval-Augmented Generation (RAG)** powered by **Google Gemini**, **FastAPI**, **PostgreSQL**, and **PGVector**.

---

## 🚀 Overview

AegisGPT is an enterprise-grade AI document assistant that enables users to upload PDFs, index their content using vector embeddings, perform semantic search, and interact with documents through natural language conversations.

The system combines modern backend technologies with Large Language Models (LLMs) to provide accurate, context-aware responses using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

### 📄 Document Management

- Upload PDF documents
- Store metadata in PostgreSQL
- Automatic document parsing
- Intelligent text chunking

### 🧠 AI & RAG

- Semantic search using PGVector
- Sentence Transformer embeddings
- Google Gemini integration
- Context-aware AI responses
- Retrieval-Augmented Generation (RAG)

### 💬 Conversations

- Persistent chat history
- Conversation management
- Multi-turn document Q&A
- AI response storage

### ⚡ Backend

- FastAPI
- Async SQLAlchemy
- Alembic migrations
- Dockerized services
- PostgreSQL
- REST APIs

---

# 🏗️ System Architecture

```text
                   +----------------------+
                   |      React UI        |
                   +----------+-----------+
                              |
                              |
                              ▼
                    +------------------+
                    |     FastAPI      |
                    +------------------+
                     |       |        |
                     |       |        |
                     ▼       ▼        ▼
               PostgreSQL  PGVector  Gemini
                     |        |        |
                     +--------+--------+
                              |
                              ▼
                      Retrieval-Augmented
                           Generation
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python |
| Database | PostgreSQL |
| Vector Database | PGVector |
| ORM | SQLAlchemy |
| Migration | Alembic |
| AI Model | Google Gemini |
| Embeddings | Sentence Transformers |
| Authentication | JWT (In Progress) |
| Containerization | Docker |
| API Documentation | Swagger UI |

---

# 📂 Project Structure

```
AegisGPT/
│
├── backend/
│   ├── app/
│   ├── migrations/
│   ├── storage/
│   ├── requirements.txt
│   └── main.py
│
├── docs/
│
├── frontend/          (Coming Soon)
│
├── docker-compose.yml
│
├── README.md
│
└── LICENSE
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Balaganesh1122/Aegisgpt-.git
cd Aegisgpt-
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Configure Environment

Create

```
backend/.env
```

Example

```env
DATABASE_URL=
SECRET_KEY=
GEMINI_API_KEY=
GEMINI_MODEL=
```

---

## Run Docker

```bash
docker compose up -d
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📌 Current APIs

| Module | Status |
|----------|--------|
| Authentication | ✅ |
| Upload Documents | ✅ |
| Semantic Search | ✅ |
| RAG Chat | ✅ |
| Conversations | ✅ |
| Messages | ✅ |

---

# 🗄️ Database

Current tables

- Users
- Documents
- Document Chunks
- Conversations
- Messages

---

# 📈 Project Status

| Module | Progress |
|----------|----------|
| Backend | ✅ Complete |
| AI Integration | ✅ Complete |
| Vector Search | ✅ Complete |
| Conversation Memory | ✅ Complete |
| Frontend | 🚧 In Progress |

---

# 🚀 Roadmap

- [x] FastAPI Backend
- [x] PostgreSQL Integration
- [x] PGVector
- [x] PDF Upload
- [x] Semantic Search
- [x] Google Gemini
- [x] RAG Pipeline
- [x] Persistent Conversations
- [ ] React Frontend
- [ ] Authentication UI
- [ ] Admin Dashboard
- [ ] Multi-document Chat
- [ ] Deployment

---

# 📚 Documentation

Backend API documentation is available inside

```
docs/Backend_API_Documentation.md
```

---

# 👨‍💻 Author

**Golla Bala Ganesh**

B.Tech Computer Science & Engineering

AI | Full Stack Development | Backend Engineering

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star.
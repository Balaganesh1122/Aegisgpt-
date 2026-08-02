# AegisGPT System Architecture

## High-Level Architecture

```text
                        +---------------------------+
                        |        React Frontend     |
                        +-------------+-------------+
                                      |
                                      |
                                      ▼
                           +----------------------+
                           |      FastAPI API     |
                           +----------+-----------+
                                      |
             +------------------------+------------------------+
             |                        |                        |
             ▼                        ▼                        ▼
      Authentication          Document Service         Conversation Service
             |                        |                        |
             ▼                        ▼                        ▼
        PostgreSQL            Ingestion Pipeline         Chat History
                                      |
                                      ▼
                              Embedding Service
                                      |
                                      ▼
                                 PGVector Search
                                      |
                                      ▼
                              Google Gemini 3.5
                                      |
                                      ▼
                              AI Generated Answer
```

---

# Request Flow

```text
User Uploads PDF
        │
        ▼
FastAPI Upload API
        │
        ▼
Save PDF
        │
        ▼
Extract Text
        │
        ▼
Chunk Text
        │
        ▼
Generate Embeddings
        │
        ▼
Store in PGVector
```

---

# Chat Flow

```text
User Question
        │
        ▼
Embedding Generation
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Top Chunks
        │
        ▼
Prompt Construction
        │
        ▼
Google Gemini
        │
        ▼
AI Response
        │
        ▼
Save Conversation
```

---

# Database Design

```text
Users
  │
  ├────────────── Documents
  │                     │
  │                     ▼
  │             Document Chunks
  │
  ▼
Conversations
       │
       ▼
Messages
```

---

# Technologies

- FastAPI
- Python
- PostgreSQL
- PGVector
- SQLAlchemy
- Alembic
- Docker
- Sentence Transformers
- Google Gemini
- JWT Authentication (Upcoming)
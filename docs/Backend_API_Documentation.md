# Backend API Documentation

## AegisGPT REST API

Version: **v1.0**

Base URL

```
http://127.0.0.1:8000/api/v1
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Authentication

## Register User

### Endpoint

```
POST /auth/register
```

### Request

```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "Password123"
}
```

### Response

```json
{
  "id": 1,
  "full_name": "John Doe",
  "email": "john@example.com"
}
```

---

## Login

### Endpoint

```
POST /auth/login
```

### Request

```json
{
  "email": "john@example.com",
  "password": "Password123"
}
```

### Response

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

# Document APIs

## Upload PDF

### Endpoint

```
POST /documents/upload
```

### Content Type

```
multipart/form-data
```

### Request

| Field | Type |
|--------|------|
| file | PDF |

### Response

```json
{
  "message": "Document uploaded successfully.",
  "document": {
    "id": 5,
    "filename": "uuid.pdf",
    "original_filename": "resume.pdf",
    "file_type": "application/pdf",
    "file_size": 325678
  }
}
```

---

# Semantic Search

## Search Similar Chunks

### Endpoint

```
POST /search
```

### Request

```json
{
  "question": "Explain the work experience.",
  "top_k": 5
}
```

### Response

```json
[
  {
    "document_id": 5,
    "chunk_index": 3,
    "content": "...",
    "distance": 0.12
  }
]
```

---

# AI Chat (RAG)

## Chat with Document

### Endpoint

```
POST /chat
```

### Request

```json
{
  "question": "Summarize this resume",
  "document_id": 5,
  "conversation_id": null,
  "top_k": 5
}
```

### Response

```json
{
  "answer": "The document is a resume of...",
  "conversation_id": 1
}
```

---

# Conversations

## Conversation Table

Stores every chat session.

Fields

| Column | Description |
|----------|-------------|
| id | Conversation ID |
| title | Auto-generated title |
| user_id | User |
| document_id | Related document |
| created_at | Creation timestamp |
| updated_at | Last update |

---

# Messages

Stores every user and AI message.

| Column | Description |
|----------|-------------|
| id | Message ID |
| conversation_id | Parent conversation |
| role | user / assistant |
| content | Message |
| created_at | Timestamp |

---

# Error Responses

## 400 Bad Request

```json
{
  "detail": "Unsupported file type."
}
```

---

## 401 Unauthorized

```json
{
  "detail": "Invalid credentials."
}
```

---

## 404 Not Found

```json
{
  "detail": "Document not found."
}
```

---

## 500 Internal Server Error

```json
{
  "detail": "Unexpected server error."
}
```

---

# Database Schema

```
Users
   │
   ├──────── Documents
   │              │
   │              ▼
   │      Document Chunks
   │
   ▼
Conversations
      │
      ▼
Messages
```

---

# AI Pipeline

```
PDF Upload
      │
      ▼
Document Parser
      │
      ▼
Text Chunker
      │
      ▼
Embedding Generator
      │
      ▼
PGVector Storage
      │
      ▼
Semantic Search
      │
      ▼
Google Gemini
      │
      ▼
AI Response
```

---

# Current Version

```
v1.0
```

---

# Future Enhancements

- JWT Role-Based Authentication
- Multi-document Chat
- Streaming Responses
- Citation Support
- Conversation Export
- Chat History UI
- Admin Dashboard
- REST + WebSocket Support
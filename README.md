<div align="center">

# ⬛ TaskFlow

### A lightweight Task Manager REST API built with FastAPI + PostgreSQL

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

</div>

---

## 📋 Overview

**TaskFlow** is a clean, layered REST API for managing tasks. It provides full **CRUD** operations via HTTP and ships with a modern **single-file frontend** featuring dark navy / light white theme switching — no build tools required.

---

## 🗂 Project Structure

```
app on fastapi/
├── app/
│   ├── main.py                   # FastAPI app entry point, CORS, lifespan
│   ├── core/
│   │   └── config.py             # Settings dataclass (DB URL, CORS origins)
│   ├── db/
│   │   └── session.py            # SQLAlchemy engine + session factory
│   ├── models/
│   │   ├── base.py               # DeclarativeBase
│   │   └── task.py               # TaskOrm model
│   ├── schemas/
│   │   └── schemas.py            # Pydantic schemas (Task, Create, Update)
│   ├── repositories/
│   │   └── task.py               # Data access layer (get_all, get_by_id, create, delete)
│   ├── services/
│   │   └── task.py               # Business logic, domain exceptions
│   └── api/
│       └── routers/
│           ├── task.py           # Route handlers
│           └── dependencies.py   # Dependency injection: get_task_service
└── index.html                    # Frontend (single file, no build step)
```

---

## ⚙️ Requirements

| Dependency | Version | Notes |
|---|---|---|
| Python | 3.12+ | Uses `X \| Y` union syntax |
| PostgreSQL | 14+ | Must be running before server start |
| fastapi | latest | Web framework |
| sqlalchemy | 2.x | Uses 2.0-style `select()` |
| psycopg2 | latest | PostgreSQL driver |
| pydantic | v2 | Uses `ConfigDict(from_attributes=True)` |
| uvicorn | latest | ASGI server |

---

## 🚀 Installation & Setup

**1. Clone the repo and create a virtual environment**

```bash
git clone <repo-url>
cd "app on fastapi"

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
```

**2. Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

**3. Configure the database**

Edit `app/core/config.py`:

```python
data_base_url = "postgresql+psycopg2://USER:PASSWORD@HOST:5432/DB_NAME"
```

**4. Start PostgreSQL, then run the server**

```bash
uvicorn app.main:app --reload
```

> 🟢 Server starts at **http://127.0.0.1:8000**  
> Tables are created automatically on first run via the lifespan hook.

**5. Open the frontend**

Open `index.html` in any browser — no build step or local server needed.

---

## 📡 API Reference

**Base URL:** `http://127.0.0.1:8000`

| Method | Endpoint | Status | Description |
|---|---|---|---|
| `GET` | `/tasks` | 200 | Get all tasks |
| `POST` | `/tasks/` | 201 | Create a new task |
| `PATCH` | `/tasks/{task_id}` | 200 | Update title and/or completed |
| `DELETE` | `/tasks/{task_id}` | 204 | Delete a task |

### Examples

<details>
<summary><b>POST /tasks/ — Create a task</b></summary>

```json
// Request body
{
  "title": "Buy groceries"
}

// Response 201 Created
{
  "id": "abe22d97-c0c0-47b2-abfa-38fcd4a105ad",
  "title": "Buy groceries",
  "completed": false
}
```

</details>

<details>
<summary><b>PATCH /tasks/{task_id} — Update a task</b></summary>

```json
// Request body (all fields optional)
{
  "title": "Buy groceries and cook",
  "completed": true
}

// Response 200 OK
{
  "id": "abe22d97-c0c0-47b2-abfa-38fcd4a105ad",
  "title": "Buy groceries and cook",
  "completed": true
}
```

</details>

<details>
<summary><b>DELETE /tasks/{task_id} — Delete a task</b></summary>

```
// Response 204 No Content
// (empty body)
```

</details>

---

## 🏗 Architecture

The project follows a strict **layered architecture** — each layer has one responsibility and depends only on the layer below it.

```
HTTP Request
     ↓
  Router          → parses request, raises HTTPException
     ↓
  Service         → business logic, commits transactions, raises TaskNotFound
     ↓
  Repository      → all SQLAlchemy queries, no business logic
     ↓
  ORM Model       → TaskOrm table definition
```

| Layer | File | Responsibility |
|---|---|---|
| **Router** | `api/routers/task.py` | HTTP handling, status codes, error mapping |
| **Service** | `services/task.py` | Orchestrates repo calls, owns transactions |
| **Repository** | `repositories/task.py` | All DB queries via SQLAlchemy |
| **Model** | `models/task.py` | `TaskOrm` table definition |
| **Schema** | `schemas/schemas.py` | Request validation & response serialization |

---

## 🖥 Frontend

A single `index.html` — no framework, no build tools, no dependencies.

| Feature | Details |
|---|---|
| 🎨 Theme toggle | Dark navy ↔ Light white, saved in `localStorage` |
| 📊 Progress bar | Shows completed vs total tasks |
| 🔍 Filter tabs | All / Active / Done |
| ✏️ Inline edit | Double-click to edit, `Enter` to save, `Escape` to cancel |
| ⚡ Optimistic UI | Updates instantly, rolls back on API error |
| 🔔 Toast notifications | Success / error / info for every action |

**Configure the API URL** at the top of the `<script>` block:

```js
const API = 'http://127.0.0.1:8000';
```

---

## ⚠️ Known Issues

- **CORS** — middleware must be registered **before** `include_router` in `main.py`
- **SessionLocal** — uses SQLAlchemy 2.x syntax: `sessionmaker[Session](bind=engine)`
- **task_id** — is a string UUID; always send the exact `id` returned by the API
- **DELETE** — returns `204 No Content`; don't attempt to parse a response body

---

<div align="center">

Made with ❤️ using **FastAPI** · **SQLAlchemy** · **PostgreSQL**

</div>

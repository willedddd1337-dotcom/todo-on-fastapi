TaskFlow — FastAPI Task Manager
Overview
TaskFlow is a lightweight REST API for managing tasks, built with FastAPI and SQLAlchemy. It exposes full CRUD operations over HTTP and ships with a modern single-file frontend with dark/light theme switching.

Project Structure
app on fastapi/
├── app/
│   ├── main.py                  # FastAPI app, CORS middleware, lifespan
│   ├── core/
│   │   └── config.py            # Settings dataclass (DB URL, CORS origins)
│   ├── db/
│   │   └── session.py           # SQLAlchemy engine + session factory
│   ├── models/
│   │   ├── base.py              # DeclarativeBase
│   │   └── task.py              # TaskOrm model
│   ├── schemas/
│   │   └── schemas.py           # Pydantic schemas (Task, Create, Update)
│   ├── repositories/
│   │   └── task.py              # DB access layer
│   ├── services/
│   │   └── task.py              # Business logic layer
│   └── api/
│       └── routers/
│           ├── task.py          # Route handlers
│           └── dependencies.py  # DI: get_task_service
index.html                       # Frontend (single file, no build step)

Requirements

Python 3.12+
PostgreSQL 14+
fastapi
sqlalchemy 2.x
psycopg2
pydantic v2
uvicorn


Installation & Setup
1. Create and activate virtual environment
bashpython -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
2. Install dependencies
bashpip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
3. Configure the database
Edit app/core/config.py:
pythondata_base_url = "postgresql+psycopg2://USER:PASSWORD@HOST:5432/DB_NAME"
4. Start PostgreSQL, then run the server:
bashuvicorn app.main:app --reload
# http://127.0.0.1:8000
# Tables are created automatically on first run
5. Open the frontend
Open index.html in any browser — no build step needed.

API Reference
Base URL: http://127.0.0.1:8000
MethodEndpointDescriptionGET/tasksGet all tasksPOST/tasks/Create a task — body: { "title": "..." }PATCH/tasks/{task_id}Update title and/or completedDELETE/tasks/{task_id}Delete a task — 204 No Content
Create task
json// POST /tasks/
{ "title": "Buy groceries" }

// 201 Created
{ "id": "uuid", "title": "Buy groceries", "completed": false }
Update task
json// PATCH /tasks/{task_id}
{ "title": "Buy groceries", "completed": true }

// 200 OK
{ "id": "uuid", "title": "Buy groceries", "completed": true }

Architecture
Router → Service → Repository → ORM Model
LayerResponsibilityRouterHTTP handling, raises HTTPExceptionServiceBusiness logic, commits transactions, raises TaskNotFoundRepositoryAll SQLAlchemy queriesModelTaskOrm table definitionSchemaPydantic request validation and response serialization

Frontend (index.html)
Single HTML file, no framework, no build tools.

Dark navy / light white theme toggle — saved in localStorage
Progress bar (completed vs total)
Filter tabs: All / Active / Done
Add task with Enter or button
Inline edit on double-click (Enter to save, Escape to cancel)
Optimistic UI — updates instantly, rolls back on error
Toast notifications for every action

API URL is configured at the top of the script:
jsconst API = 'http://127.0.0.1:8000';

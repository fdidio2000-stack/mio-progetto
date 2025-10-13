# 📇 Contacts API

A modern, containerized RESTful API for managing contacts built with FastAPI, SQLite, and Docker. It supports full CRUD operations, contact enrichment via external avatar providers, email validation, and includes both unit and integration tests.

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-FastAPI-green" />
  <img src="https://img.shields.io/badge/Database-SQLite-blue" />
  <img src="https://img.shields.io/badge/Tested%20with-Pytest-yellow" />
  <img src="https://img.shields.io/badge/Containerized-Docker-blue" />
</p>

---

## 📖 Table of Contents

- Features
- Technologies
- API Overview
- Project Structure
- Getting Started
- Running the Project (Docker)
- Testing
- Environment Variables
- External Services Used
- Future Improvements

---

## ✨ Features

- Create, Read, Update, Delete (CRUD) contacts
- External avatar enrichment (Gravatar, DiceBear, etc.)
- Optional email and phone validation via public APIs
- Pagination and filtering
- Clean architecture (Routers, CRUD, Services)
- Unit tests + Integration tests (with mock external services)
- Dockerized environment
- REST docs with Swagger UI (via FastAPI)

---

## 🧰 Technologies & Techniques Used

| Category              | Stack / Tools                                  |
|----------------------|--------------------------------------------------|
| API Framework         | FastAPI                                         |
| Language              | Python 3.11+                                     |
| Database              | SQLite (via SQLAlchemy 2.0 ORM)                 |
| Validation            | Pydantic                                         |
| External APIs         | Gravatar, DiceBear, RandomUser, Veriphone (opt) |
| Testing               | Pytest, Pytest-asyncio, httpx                   |
| Mocking               | monkeypatch / unittest.mock                     |
| Dev Tools             | Docker, Docker Compose, Makefile                |
| Docs                  | FastAPI + Swagger UI                            |

---

## 🧪 API Overview

All endpoints are prefixed with /contacts:

- POST /contacts → Create a contact (with optional avatar enrichment)
- GET /contacts → List contacts (with search, tags, pagination)
- GET /contacts/{id} → Retrieve contact by ID
- PUT /contacts/{id} → Update contact (re-fetch avatar if email changes)
- DELETE /contacts/{id} → Delete contact

Example contact object:

```json
{
  "id": 1,
  "full_name": "Alice Smith",
  "email": "alice@example.com",
  "phone": "+123456789",
  "tags": ["client", "vip"],
  "avatar_url": "https://...",
  "created_at": "2025-10-10T12:00:00Z",
  "updated_at": "2025-10-10T13:00:00Z"
}
```

## 🗂️ Project Structure
```graphql
contacts-api/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── db.py                # DB engine, session management
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # DB access logic
│   ├── routers/
│   │   └── contacts.py      # API routes
│   └── services/
│       └── enrich.py        # Avatar & email enrichment logic
├── tests/
│   ├── unit/
│   └── integration/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

---

# #🚀 Getting Started
Clone the repository:
```
git clone https://https://github.com/fdidio2000-stack/mio-progetto/tree/main/contacts-api
cd contacts-api
```
(Optional) Create a virtualenv for local testing:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
Start the app locally:

```
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs
 for Swagger UI.

---

# #🐳 Running with Docker

Build the image:
```
docker build -t contacts-api .
```

Run the container:
```
docker run -p 8000:8000 contacts-api

```
Or use docker-compose:
```
docker compose up --build
```
---

# ✅ Running Tests

Run all tests:
```
pytest
```

Or via Makefile:
```
make test
```

Test types:

Unit tests: test CRUD logic and services with mocks

Integration tests: full API coverage using FastAPI TestClient

---

## ⚙️ Environment Variables

Use a .env file or export variables at runtime:

| Variable         | Description                    | Example                       |
|------------------|--------------------------------|-------------------------------|
| AVATAR_PROVIDER | Which avatar service to use    | gravatar, dicebear            |
| DB_URL          | SQLAlchemy database URI        | sqlite:///./contacts.db       |

In Docker, you can mount a .env file or inject variables via docker-compose.

---

## 🌐 External Services Used

| Service     | Purpose                    | Docs / Link                                       |
|-------------|----------------------------|--------------------------------------------------|
| Gravatar    | Avatar by email hash       | https://en.gravatar.com/site/implement/images/   |
| DiceBear    | Avatar generation via seed | https://www.dicebear.com                         |
| RandomUser  | Fake contact data (dev)    | https://randomuser.me/api                        |
| Veriphone   | (Optional) Phone validation| https://veriphone.io                             |

All external calls are isolated and mockable in tests.

---

## 📌 Future Improvements

- JWT Authentication
- Role-based access (Admin vs User)
- Rate limiting
- Webhook events for audit service
- Switch DB to PostgreSQL for production
- Swagger auth & environment support

# 🧑‍💻 Author
Made with ❤️ by [Your Name] — open to contributions, ideas, and pull requests.
```

Fammi sapere se vuoi:

- una versione in italiano 🇮🇹
- una versione con badge CI/CD (GitHub Actions, ecc.)
- il file in formato PDF/Word
- l’upload automatico su GitHub


```
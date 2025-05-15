# ☕ Explore Cafe API – FastAPI + PostgreSQL

A professional, production-ready REST API for managing cafes, built with **FastAPI**, **PostgreSQL**, and structured using the **12-Factor App principles** with a focus on future-ready ML microservice design.

---

## Project Purpose

This project serves as a demonstration of how to build a clean, maintainable, containerized backend service using FastAPI. It enables:

* Creation and retrieval of cafe information
* Validation of structured data (Wi-Fi availability, location, etc.)
* Clean, modular project structure
* Proper environment configuration and deployment pipeline
* ML-ready architecture using modern best practices

---

##  Applied 12-Factor App Principles (ML-Oriented)

This project applies the [12-Factor App methodology](https://12factor.net/) with ML-oriented best practices and workflows, focusing on scalability, maintainability, and portability.

| Principle                  | Implementation                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1. Codebase**            | Git-managed and hosted on GitHub                                                                             |
| **2. Dependencies**        | Isolated using `venv`, tracked in `requirements.txt`                                                         |
| **3. Config**              | Managed via `.env` file and Pydantic `BaseSettings`                                                          |
| **4. Backing Services**    | PostgreSQL is treated as an external service via Docker Compose                                              |
| **5. Build, Release, Run** | Separate build (`Dockerfile`), release (`docker-compose`), and run phases; image pushed to Docker Hub        |
| **6. Port Binding**        | FastAPI binds to port `8000`, PostgreSQL to `5432`                                                           |

---

##  Tech Stack

*  Python 3.11+
*  FastAPI
*  PostgreSQL
*  asyncpg 
*  Docker & Docker Compose
*  Pytest


---


##  Features

This API provides full CRUD (Create, Read, Update, Delete) functionality for managing cafes, based on the [API specification documented here](https://documenter.getpostman.com/view/37746097/2sB2qWFPDa#239373f3-3120-45b7-958c-5aba10fa3dbe).

### 🔗 Common Cafe API Endpoints

| Method   | Endpoint                       | Description                                     |
| -------- | ------------------------------ | ----------------------------------------------- |
| `GET`    | `/cafes/`                      | Get a list of all cafes                         |
| `GET`    | `/cafes/{cafe_id}`             | Get a specific cafe by ID                       |
| `POST`   | `/cafes/addcafe`               | Add a new cafe to the database                  |
| `PUT`    | `/cafes/update_cafe/{cafe_id}` | Update an existing cafe by ID                   |
| `DELETE` | `/cafes/delete_cafe/{cafe_id}` | Delete a cafe by ID (requires secret key query) |


---


##  Running Instructions

###  Run Locally (No Docker)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env  # Then edit as needed

# Run the app
uvicorn app.main:app --reload
```

Access the app at: `http://localhost:8000/docs`

---

###  Run with Docker

```bash
docker-compose up --build
```

* API: [http://localhost:8000/cafes](http://localhost:8000/cafes)
* Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* Docker-Hub Repo []()

---

## 📁 Project Setup & Config Notes

* All environment variables are managed in `.env`
* The `app/main.py` file handles FastAPI initialization and DB table creation
* PostgreSQL is managed via Docker Compose as a backing service
* Tables are created at runtime using SQLAlchemy's metadata

###  Example `.env` file

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=cafe_db
DB_HOST=db
DB_PORT=5432

FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
```

---

##  Testing

Run tests locally:

```bash
pytest
```

### Test Functions

1. **`test_get_all_cafes`**

   * **Purpose**: Tests the `/cafes/` endpoint to fetch all cafes.
   * **Outcome**: Verifies that the endpoint returns a list of cafes with the correct status code (200) and that the returned data contains the expected structure for each cafe.

2. **`test_create_cafe`**

   * **Purpose**: Tests the `/cafes/addcafe` endpoint to create a new cafe.
   * **Outcome**: Verifies that a new cafe is successfully created with a status code of 201, and the returned data matches the input.


---



## 🎬 Demo

| Description      | Link                                                       |
| ---------------- | ---------------------------------------------------------- |
|   API Demo       | *Coming soon or self-hosted*                               |
|  Pytest Output   | [Output](https://github.com/KushalRegmi61/Explore-Cafe-API/blob/master/results/pytest-output.png)               |




---


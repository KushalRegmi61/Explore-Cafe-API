# ExploreCafe API

This is a FastAPI-based project to explore cafes.

## Features
- List cafes
- Dockerized for easy deployment
- CI/CD with GitHub Actions

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Database Setup

1. Start the PostgreSQL service using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Apply the database schema:
   ```bash
   docker exec -i <container_name> psql -U postgres -d cafe_db < app/db/schema.sql
   ```

Replace `<container_name>` with the name of your PostgreSQL container.

## Testing
Run tests with:
```bash
pytest
```

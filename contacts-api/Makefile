.PHONY: run test up down fmt
run:
uvicorn app.main:app --reload
test:
pytest -q
up:
docker compose up --build -d
down:
docker compose down -v

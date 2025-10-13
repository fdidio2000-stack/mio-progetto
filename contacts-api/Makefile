.PHONY: run test up down fmt
run:
\tuvicorn app.main:app --reload
test:
\tpytest -q
up:
\tdocker compose up --build -d
down:
\tdocker compose down -v

.PHONY: test build run lint clean

test:
	cd app && pytest -v tests/

lint:
	pip install ruff
	ruff check app/

build:
	docker build -t github-actions-cicd:local .

run:
	docker compose up -d --build

clean:
	docker compose down -v --remove-orphans

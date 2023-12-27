init:
	# python -m venv venv
	# source venv/scripts/activate
	# poetry install
	docker-compose up -d

start:
	poetry run uvicorn src.main:app --reload

migration:
	python -m migrations.env
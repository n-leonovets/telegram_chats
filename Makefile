start:
	# python -m venv venv
	# source venv/scripts/activate
	# poetry install
	poetry run uvicorn src.main:app --reload
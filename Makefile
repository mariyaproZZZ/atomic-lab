.PHONY: install lint test run clean

# Create virtual environment and install dependencies
install:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.lock.txt
	venv\Scripts\activate && pip install black flake8 pytest

# Check code style
lint:
	venv\Scripts\black --check app.py test_app.py
	venv\Scripts\flake8 app.py test_app.py --max-line-length=88

# Run tests
test:
	venv\Scripts\pytest test_app.py -v

# Run application
run:
	venv\Scripts\python app.py

# Clean temporary files
clean:
	rmdir /s /q venv
	del /s /q *.pyc
	del /s /q __pycache__

## Steps to setup the backend

### Create a virtual environment
- python -m venv env

- pip install -r requirements.txt
- uvicorn main:app --host 0.0.0.0 --port 8000

### For running the test
- pytest
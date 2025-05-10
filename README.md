# FastAPI Hexagonal Architecture Scaffold

This repository contains a scaffold for a FastAPI project following the principles of hexagonal architecture. It includes:

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Hexagonal Architecture**: Ensures separation of concerns and modularity.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

- `main.py`: Entry point of the application.
- `requirements.txt`: Lists the dependencies.
- `.github/copilot-instructions.md`: Custom instructions for Copilot.

## Contributing

Feel free to fork this repository and submit pull requests for improvements.
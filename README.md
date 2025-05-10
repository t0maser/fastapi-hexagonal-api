# Plantilla de Arquitectura Hexagonal con FastAPI

Este proyecto es una plantilla para construir APIs utilizando FastAPI con una arquitectura hexagonal. Proporciona una estructura modular y limpia para comenzar rápidamente.

## Características
- **FastAPI**: Un framework moderno y rápido para construir APIs con Python.
- **Arquitectura Hexagonal**: Un patrón de diseño que promueve la separación de responsabilidades y la modularidad.

## Cómo Empezar

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

3. Accede a la documentación de la API en:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación.
- `adapters/`: Contiene los adaptadores de la API.
- `application/`: Contiene los servicios y casos de uso.
- `domain/`: Contiene las entidades y lógica de negocio.
- `infrastructure/`: Contiene configuraciones y detalles técnicos.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.
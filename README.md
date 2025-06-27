# Frontend - Sistema RAG con Agentes

Este es el frontend del sistema conversacional basado en RAG. Utiliza Streamlit para proporcionar una interfaz web interactiva desde la cual el usuario puede realizar preguntas, visualizar respuestas y explorar los resultados proporcionados por el backend.

## Requisitos previos

- Python 3.10+
- pip
- Entorno virtual (recomendado)

## Instalación

1. Clona el repositorio y accede al directorio del frontend:
   ```bash
   git clone https://github.com/manuelvico0102/App-Agentic-RAG-frontend.git
   cd App-Agentic-Rag-frontend
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Mac/Linux
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```


## Ejecutar

Lanza la aplicación localmente con:

```bash
streamlit run app.py
```

Esto abrirá una interfaz en el navegador por defecto disponible en `http://localhost:8501`.

## Levantar el sistema completo con Docker Compose

Puedes ejecutar tanto el backend como el frontend juntos utilizando Docker Compose. Para ello:

1. Sitúa el archivo `docker-compose.yml` a la misma altura que las carpetas `backend/` y `frontend/`.

2. Ejecuta el siguiente comando desde esa ubicación:

```bash
docker compose up --build
```

Esto construirá y levantará los servicios necesarios, y podrás acceder a la aplicación desde tu navegador.

## Notas

- El frontend está pensado para conectarse con el backend desarrollado en FastAPI, siendo el de [App-Agentic-RAG](https://github.com/manuelvico0102/App-Agentic-Rag).
- Asegúrate de que ambos servicios estén corriendo simultáneamente para un funcionamiento completo.
- Puedes configurar las direcciones del backend en un archivo de configuración o mediante variables de entorno.

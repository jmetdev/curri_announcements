# Introduction

Accepts POST and HEAD requests. A request to a path (e.g. `/<greetingName>`) renders a CURRI XML response that instructs Cisco UCM to play the announcement with that name. The CURRI XML is produced from a **Jinja template** (`templates/announcement.xml`); the greeting name from the URI is passed into the template as `name` (escaped for safety).

HEAD requests to `/` are used for keep-alives that Cisco Communications Manager sends to check if the ECC URL is up.

# Example

`https://localhost/MonitoringWarning_00055` renders XML that instructs the UCM to play the announcement named `MonitoringWarning_00055`.

# How to run the Flask server

**Development (Flask built-in server):**

```bash
pip install -r requirements.txt
python app.py
```

Server listens on `http://0.0.0.0:5000`.

**Production (Gunicorn):**

```bash
pip install -r requirements.txt
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Server listens on `http://0.0.0.0:8000`.

**Docker:**

```bash
docker compose up --build
```

See the Docker section below for the Dockerfile and Compose setup.

# Docker

- **Dockerfile**: Builds a Python image, installs dependencies, and runs the app with Gunicorn on port 8000.
- **Docker Compose**: Runs the app as a service; the Flask app is exposed on port 8000 (e.g. `http://localhost:8000`).

# HyeTech Networks

Designed by Jeff Metcalf 06/24/2021

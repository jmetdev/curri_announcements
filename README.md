# Introduction

This service returns CURRI XML so Cisco UCM can play an announcement. The URL path is the announcement name (e.g. `/MonitoringWarning_00055`). Announcements are managed in UCM under **Media Resources → Announcements**.

# Example

`http://{{ServerIP}}/MonitoringWarning_00055` renders XML that instructs the UCM to play the announcement named `MonitoringWarning_00055`.

# Cisco Call Manager configuration

Luckily Cisco gives us a stock, "Your call is being monitored or recorded message, called MonitoringWarning_00055" If you dont need anything fancy just use that.

Configure the External Call Control profile in UCM so it uses this service:

1. In **Cisco Unified CM Administration**, go to **Call Routing → External Call Control Profile**.
2. Create or edit a profile (e.g. for call recording announcements).
3. Set **Primary Web Service** to the base URL of this app plus the greeting name as the path:
   - Example: `http://10.10.10.10:8000/MonitoringWarning_00055`  
     UCM will send requests to that URL; this app will respond with CURRI XML for the announcement named `MonitoringWarning_00055`.
4. **Secondary Web Service** is optional (backup URL).
5. **Call Treatment on Failures** (e.g. "Allow Calls") controls behavior when this service is unreachable.

6. **Apply the ECC profile** to the calls that should use this service. In UCM Admin, open the configuration for the pattern or number you want to control, then set **External Call Control Profile** to the profile you created (e.g. "Call Recording Announcment"). You can attach the profile to:
   - **Directory Number** — Call Routing → Directory Number Configuration; set **External Call Control Profile** on the directory number (e.g. 1234).
   - **Route Pattern** — Call Routing → Route Plan Report or Route Pattern; set **External Call Control Profile** on the route pattern.
   - **Translation Pattern** — Call Routing → Translation Pattern; set **External Call Control Profile** on the translation pattern.
   - **Other patterns** — Any pattern type that supports an External Call Control Profile can use the same profile.

The path segment in the Primary Web Service URL is the greeting/announcement name that is passed into the Jinja template. Ensure the UCM server can reach the host and port where this Flask app is running (e.g. `10.10.10.10:8000`).

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

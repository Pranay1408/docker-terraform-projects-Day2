# Day2: Flask + MySQL Docker Project

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Docker](https://img.shields.io/badge/Docker-Compose-blue) ![License](https://img.shields.io/badge/License-MIT-green)

A simple **Flask application** connected to a **MySQL database** using **Docker Compose**.  

---

## **Project Structure**

The project already contains:  
- `docker-compose.yml`  
- `app/` folder with `Dockerfile`, `app.py`, `requirements.txt`  

---

## **Setup & Run**

1. Navigate to the project folder:

```bash
cd day2-flask-mysql
Build and start containers:
docker-compose up -d --build
Check running containers:
docker-compose ps
Access the Flask app:
http://<your-host-IP>:5000
Notes
Make sure ports 5000 (Flask) and 3306 (MySQL) are open in firewall/security groups.
Flask app runs in development mode; for production, consider using Gunicorn.
Terraform code is excluded from this repo.

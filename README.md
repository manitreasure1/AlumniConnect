# AlumniConnect

## 📌 Project Overview

AlumniConnect is a web platform that allows former students to register, select courses, pick houses, and receive approval from the senior house master. The platform ensures a seamless registration process and effective management of alumni data.

## 🚀 Features

- **User Registration & Authentication** (JWT-based authentication)
- **Course Selection System**
- **House Selection Module**
- **Senior House Master Approval System**
- **Admin Dashboard for Management**

## 🛠️ Tech Stack

### Backend

- **Framework:** Flask
- **Database:** PostgreSQL
- **Authentication:** JWT
- **ORM:** SQLAlchemy
- **Migrations:** Flask-Migrate

### Frontend

- **Framework:** React

- **UI Framework:** React-Bootstrap&#x20;

## 📂 Project Structure

```
alumni_connect/
backend/  (Flask API)
│── app/
│   ├── __init__.py
│   ├── db/
|   |   |   ├──models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── students.py
│   │   ├── courses.py
│   │   ├── houses.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── student_service.py
│   ├── utils/
│   │   ├── redis.py
│   ├── config/
|   |   |   ├──config.py
|   |   |   ├──depedencies.py
│   ├── migrations/
│   ├── tests/
│   ├── .env
│   ├── requirements.txt
│   ├── run.py
│   ├── README.md
│
│── frontend/  (React App)
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   ├── package.json
│   ├── README.md
│
│── README.md
```

## ⚙️ Setup Instructions

### Backend

1. Clone the repository
   ```sh
   git clone <repo_url>
   cd AlumniConnect/backend
   ```
2. Create a virtual environment and activate it
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env` file
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/alumniconnect
   SECRET_KEY=your_secret_key_here
   ```
5. Run the application
   ```sh
   flask run
   ```

### Frontend

1. Navigate to the frontend folder
   ```sh
   cd ../frontend/alumni_connect_frontend
   ```
2. Install dependencies
   ```sh
   npm install
   ```
3. Start the development server
   ```sh
   npm start
   ```

---

**Project Manager's Notes:** This document will be updated as the project progresses. Make sure to check off completed tasks.


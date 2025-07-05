# 🏥 Patient Management System - FastAPI + MongoDB + Frontend UI

A full-stack CRUD application for managing patient records using **FastAPI**, **MongoDB**, and a responsive **HTML + JavaScript UI**.

---

## 🚀 Features

- Add / Edit / Delete patients
- Auto-calculates **BMI** and health **verdict**
- Stores data in **MongoDB**
- Simple and interactive **Bootstrap UI**
- Built with **FastAPI** and modern Python features (`pydantic`, `Field`, `Literal`)
- Supports **CORS** for frontend-backend integration

---

## 🧰 Tech Stack

| Layer      | Tech         |
|------------|--------------|
| Backend    | FastAPI, Pydantic |
| Database   | MongoDB (local or Atlas) |
| Frontend   | HTML5, Bootstrap 5, JavaScript (Vanilla) |
| Deployment | Docker-ready |

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── ...
├── frontend/
│   ├── index.html
│   └── app.js
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/patient-management-fastapi.git
cd patient-management-fastapi
```

### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn pymongo motor python-multipart
```

### 3. Start MongoDB Locally

> Make sure `mongod` is running on `mongodb://localhost:27017`

### 4. Run FastAPI

```bash
uvicorn main:app --reload
```

- Access Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Run Frontend

Open `frontend/index.html` in your browser.

If using VS Code:

```bash
# Optional: install live server for automatic reloads
```

---

## 🐳 Docker (Optional)

Build and run container:

```bash
docker-compose up --build
```

- **Backend** → http://localhost:8000/docs
- **Frontend** → http://localhost:5500

---

## 🧠 Future Improvements

- Add login/authentication
- Pagination, search, filters
- Cloud MongoDB (MongoDB Atlas)
- React/Vue frontend
- Export as Excel/CSV

---

## 👨‍💻 Author

**Prafulla Bharate**  
🔗 [GitHub](https://github.com/prafullabharate)  
💬 FastAPI | MongoDB | Python | ML | Full Stack

---

## 📜 License

This project is licensed under the MIT License.
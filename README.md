# Expense Tracker

A web-based application for tracking personal expenses, built using Flask (backend), PostgreSQL (database), and React (frontend). The project is containerized with Docker for easy deployment.

## 📌 Features

✅ Add expenses with description, category, amount, and date.  
✅ View and manage a list of all recorded expenses.  
✅ Delete unwanted expenses.  
✅ Analyze spending with dynamic charts and graphs.  
✅ Fully containerized using **Docker** and **Docker Compose**.  

---

## 🛠️ Tech Stack

- **Backend:** Flask + SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** React.js
- **Containerization:** Docker & Docker Compose

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)  
- [Docker Compose](https://docs.docker.com/compose/)  

---

### 🛠️ Installation & Setup

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/MuhammedGam/expense-tracker.git
cd expense-tracker
```

2️⃣ **Run the application using Docker Compose:**
```sh
docker-compose up -d --build
```

3️⃣ **Access the app in your browser:**
```
Frontend:  http://localhost:3000
Backend API:  http://localhost:5000
```

4️⃣ **To stop the application:**
```sh
docker-compose down
```

---

## ⚙️ Project Structure

```
expense-tracker/
│
├── backend/                # Flask API
│   ├── app.py              # Main Flask application
│   ├── models.py           # Database models (PostgreSQL)
│   ├── routes.py           # API routes
│   ├── database.py         # Database connection
│   ├── config.py           # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend Dockerfile
│   ├── .env                # Environment variables
│
├── frontend/               # React Frontend
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   ├── package.json        # Frontend dependencies
│   ├── webpack.config.js   # Webpack configuration
│   ├── Dockerfile          # Frontend Dockerfile
│
├── docker-compose.yml      # Docker Compose file
├── README.md               # Project documentation
└── .gitignore              # Ignored files
```

---

## 📝 API Endpoints

| Method | Endpoint       | Description          |
|--------|---------------|----------------------|
| GET    | `/expenses`    | Fetch all expenses  |
| POST   | `/expenses`    | Add a new expense   |
| DELETE | `/expenses/:id` | Delete an expense  |

---

## 🛠️ Development & Contribution

### Running Locally Without Docker

1️⃣ **Backend Setup**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=5000
```

2️⃣ **Frontend Setup**
```sh
cd frontend
npm install
npm start
```

3️⃣ **Access the app:**
```
Frontend:  http://localhost:3000
Backend API:  http://localhost:5000
```

---

### Contributing

Contributions are welcome! Follow these steps:

1. Fork the repo.  
2. Create a new branch (`feature-xyz`).  
3. Make changes and test them.  
4. Commit and push to your fork.  
5. Open a pull request.  

---

## 📌 Future Enhancements

- ✅ User Authentication (Login & Signup)
- ✅ Export data as CSV/PDF
- ✅ Advanced analytics with filtering

---

## 🏆 Acknowledgments

This project was built for learning purposes and is open for improvements.

---

## 🐛 License

This project is licensed under the MIT License.

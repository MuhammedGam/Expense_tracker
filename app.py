from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import os

# Initialize Flask App
app = Flask(__name__)

# Database Path
db_path = os.path.join(os.getcwd(), "data", "expenses.db")

# Create Database if it doesn't exist
def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return render_template("index.html", expenses=rows)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        description = request.form["description"]
        category = request.form["category"]
        amount = request.form["amount"]
        date = request.form["date"]

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (description, category, amount, date) VALUES (?, ?, ?, ?)",
                       (description, category, amount, date))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_expense.html")

@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/analysis")
def analysis():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return render_template("analysis.html", data=data)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)

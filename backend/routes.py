from flask import request, jsonify
from models import db, Expense

def init_routes(app):
    @app.route("/expenses", methods=["GET"])
    def get_expenses():
        expenses = Expense.query.all()
        return jsonify([{ "id": e.id, "description": e.description, "category": e.category, "amount": e.amount, "date": e.date } for e in expenses])

    @app.route("/expenses", methods=["POST"])
    def add_expense():
        data = request.json
        new_expense = Expense(description=data["description"], category=data["category"], amount=data["amount"], date=data["date"])
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added!"}), 201

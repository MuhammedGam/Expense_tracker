# Expense Tracker

A simple web application built with Flask for tracking personal expenses.


## Description

This application helps you manage your expenses easily. You can add new expenses, view a list of expenses, delete expenses, and analyze spending (coming soon).

## Getting Started

### Prerequisites

*   Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
*   pip (Python package installer)

### Installation

1.  Clone the repository: `git clone https://github.com/MuhammedGam/expense-tracker.git`
2.  Navigate to the project directory: `cd expense-tracker`
3.  Install the required packages: `pip install Flask`

### Running the app

*   Run the application: `python app.py`
*   Open your browser and go to: `http://localhost:5000/`

## Features

*   **Add Expenses:** Add a description, category, amount, and date for each expense.
*   **View Expenses:** View a list of all recorded expenses.
*   **Delete Expenses:** Delete unwanted expenses.
*   **Expense Analysis (Coming Soon):** Charts and graphs to analyze spending by category.

## Usage

1.  **Add an Expense:**
    *   Go to `http://localhost:5000/`.
    *   Click on "Add Expense".
    *   Fill out the form with the required information.
    *   Click "Submit".

2.  **View Expenses:**
    *   The list of expenses is displayed on the main page (`http://localhost:5000/`).

3.  **Delete an Expense:**
    *   Click the "Delete" button next to the expense you want to delete.

## Development

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Make your changes.
3.  Test your changes thoroughly.
4.  Commit and push your changes to your fork.
5.  Submit a pull request.

## Additional Notes

*   This is a basic Flask application intended for learning and personal use.
*   For larger projects, consider using a more robust database like PostgreSQL or MySQL.
*   Possible future enhancements:
    *   User Authentication.
    *   Data export in various formats (CSV, PDF).
    *   Improved category management.

## 📌 Overview
Expense Tracker is a web application that helps users track their expenses, visualize financial insights, and manage budgets efficiently.

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL 
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker & Docker Compose

## 🚀 Setup Guide

### 1️⃣ Install Dependencies
```sh
pip install -r backend/requirements.txt
cd frontend && npm install

# 🚀 Project Setup Instructions

 Please follow these steps carefully to set up the project on your local machine.

---

## 1. Clone the Repository

First, pull the code from GitHub to your local machine:

```bash
git clone https://github.com/Mariam-Samy12/BudgetManagement_powerpuff.git
cd budgetproject
```

---

## 2. Create a Virtual Environment (Recommended)

To keep the dependencies isolated and avoid any conflicts, create a virtual environment:

```bash
python -m venv venv
```

> Note: You can replace the second `venv` with any name you prefer.

---

## 3. Activate the Environment

### On Windows

```bash
venv\Scripts\activate
```

### On Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

Install all the required libraries used in this project:

```bash
pip install -r requirements.txt
```

---

## 5. Database Migration

Since the database file is not included in the repository, you need to generate it locally:

```bash
python manage.py migrate
```

---

## 6. Run the Server

Finally, start the development server. If it runs, you're good to go!

```bash
python manage.py runserver
```

---

# 📁 Project Structure & File Descriptions

## `manage.py`

The command-line utility for administrative tasks such as:

- Starting the server
- Running migrations
- Creating apps
- Managing the project

---

## `budgetproject/`

The core project directory containing:

- `settings.py`
- `urls.py`
- WSGI/ASGI configuration files

---

## `budget/`

The main application folder where:

- Models
- Views
- Business Logic

reside.

---

## `db.sqlite3`

The local database file generated after migration where all budget data is stored.

---

## `requirements.txt`

A list of all Python packages and libraries needed to run the project.

---

## `templates/`

Contains the HTML files for the user interface.

---

## `static/`

Holds the CSS, JavaScript, and images used in the frontend.
# 📦 Application Modules (Apps)

## `account/` (Auth)

Handles user identity management, including:

- Sign Up
- Login
- Logout


---

## `dashboard/`

The central hub providing:

- A visual overview of the financial status
- Recent activities


---

## `transactions/`

The core module for recording:

- Income
- Expenses

with details such as:

- Category
- Amount
- Date
- Notes

---

## `budgets/`

Allows users to:

- Set spending limits
- Track expenses against budgets
- Monitor financial plans

---

## `goals/`

Dedicated to savings targets, helping users:

- Set financial goals
- Track progress
- Reach specific financial milestones

---

## `reports/`

Generates analytical insights through:

- Charts
- Financial summaries
- Expense analysis

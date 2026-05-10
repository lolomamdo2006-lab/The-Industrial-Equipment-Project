# 🚀 Project Setup Instructions

 Please follow these steps carefully to set up the project on your local machine.

---

## 1. Clone the Repository

First, pull the code from GitHub to your local machine:

```bash
git clone https://github.com/lolomamdo2006-lab/The-Industrial-Equipment-Project.git
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



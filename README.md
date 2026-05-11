# 🚀 Project Setup Instructions

 Please follow these steps carefully to set up the project on your local machine.

---

## 1. Clone the Repository

First, pull the code from GitHub to your local machine:

```bash
git clone https://github.com/lolomamdo2006-lab/The-Industrial-Equipment-Project.git
cd ourProject
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

## 6. SQL Database Setup 🗄️

follow these steps to connect it properly:

### 6.1 Install SQL Server
Make sure you have SQL Server installed (or SQL Server Express).

Also install:
- SQL Server Management Studio (SSMS)
- ODBC Driver for SQL Server
the link
(https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17&utm_source=chatgpt.com)

and do 
pip install -r requirements.txt

---

### 6.2 Create a Database
Open SQL Server and run:
the file that sama do (on whatsapp)

## 6. Environment Variables Setup (.env) 🔐

Before running the project, you need to create a `.env` file in the root directory of the project.

This file is required to store sensitive information like database credentials and secret keys.

### 6.1 Create the `.env` file

Create a file named: .env

### 6.2 Add the following variables inside `.env`

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

DB_NAME=your_database_name
DB_HOST=your host name
DB_PORT=''

# 1. Install required python packages
pip install -r requirements.txt

# 2. Apply migrations to the database
python manage.py migrate

# 3. Start the project
python manage.py runserver
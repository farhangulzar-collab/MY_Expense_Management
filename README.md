# 📘 My Expense Management  
A simple, Streamlit-based **personal expense management web app** with an analytics dashboard.  
Designed for individuals who want to track daily spending, categorize expenses, and visualize where their money goes.  
Not intended for complex business accounting or double-entry systems — just clean, simple personal expense tracking.

---

## 🚀 Features

### **1. Add / Update Expenses**
- Enter **Amount**, **Category**, and **Notes**
- Select a **Date** and update expenses for that day
- Supports editing existing entries

### **2. View Expenses by Date**
- Fetches expenses for any selected date
- Useful for daily tracking

### **3. Analytics Dashboard**
Includes:
- **Expense breakdown by category** (Bar Chart)
- **Category-wise totals and percentages** (Table)
- **Custom date range selection** for analysis

### **4. Backend API (FastAPI)**
- Handles retrieving, inserting, deleting, and summarizing expenses
- Database-powered using SQL

### **5. Simple & Intuitive UI**
- Built using **Streamlit**
- Designed for non-technical users  
- No login required  
- Works locally

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web UI  
- **FastAPI** – Backend REST API  
- **MySQL / SQL** – Database  
- **Power Query** *(optional for analytics tasks)*

---

## 📂 Project Structure

project-root/
│
├── backend/
│   ├── db_helper.py
│   ├── logging_setup.py
│   ├── my_app.log
│   ├── server.log
│   └── server.py
│
├── frontend/
│   ├── app_update_ui.py
│   ├── analytics_ui.py
│   └── app.py
│
├── testers/
│   ├── backend/
│   │   └── test_db_helper.py
│   └── frontend/
│       └── conf_test_dbhelper.py
│
├── README.md
└── requirements.txt


## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone <repository-url>
cd expense-management-system

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the FastAPI Backend
uvicorn server:app --reload
## (Run this inside the backend folder)

### 4. Run the Streamlit Frontend
streamlit run frontend/app.py


## 📊 How It Works (Summary)

1. User enters expenses → FastAPI saves them to SQL  
2. Analytics requests → Backend calculates totals & percentages  
3. Streamlit displays charts + tables for easy understanding  


## 🧑‍💻 Author  
Farhan


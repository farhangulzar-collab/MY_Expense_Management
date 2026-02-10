import mysql.connector
from contextlib import contextmanager
from logging_setup import  setup_logging

logger = setup_logging("db_helper","myapp.log")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date=%s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expenses_for_date: {expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_cursor(commit=True)  as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary: {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT category, sum(amount) as total
                       FROM expenses where expense_date
                       Between %s and %s
                       group by category"""
                       ,(start_date,end_date))
        expenses = cursor.fetchall()
        return expenses

def fetch_monthly_expenses_by_year(year):
    logger.info(f"fetch_monthly_expenses_by_year: {year}")
    with get_db_cursor() as cursor:
        # Groups data by month name and orders it by month number (1=Jan, 2=Feb, etc.)
        sql = """SELECT MONTHNAME(expense_date) as month_name, SUM(amount) as total
            FROM expenses
            WHERE YEAR(expense_date) = %s
            GROUP BY MONTHNAME(expense_date), MONTH(expense_date)
            ORDER BY MONTH(expense_date)
            """
        cursor.execute(sql, (year,))
        return cursor.fetchall()

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)
    summary=fetch_expense_summary("2024-08-01","2024-08-05")
    for record in summary:
        print(record)










"""Модуль для роботи з базою даних SQLite та аналітики замовлень через Pandas."""

import csv
import sqlite3
import pandas as pd


def create_database(db_name: str) -> None:
    """Створює базу даних та таблицю orders."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                customer_name TEXT NOT NULL,
                city TEXT NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                status TEXT NOT NULL
            )
        """)


def import_orders(csv_file: str, db_name: str) -> None:
    """Зчитує замовлення з CSV та записує їх у таблицю orders."""
    rows: list[tuple] = []

    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append((
                row["order_id"],
                row["customer_id"],
                row["customer_name"],
                row["city"],
                row["order_date"],
                float(row["total_amount"]),
                row["status"],
            ))

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.executemany(
            """
            INSERT OR REPLACE INTO orders (
                order_id, customer_id, customer_name, city, order_date, total_amount, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )


def make_top_customers_report(db_name: str, city: str, status: str = "completed") -> None:
    """Рахує ТОП-5 клієнтів у SQL, додає avg_check у Pandas і зберігає звіт у БД."""
    query = """
        SELECT
            customer_id,
            customer_name,
            COUNT(order_id) AS orders_count,
            SUM(total_amount) AS total_spent
        FROM orders
        WHERE status = ? AND city = ?
        GROUP BY customer_id, customer_name
        ORDER BY total_spent DESC
        LIMIT 5
    """

    with sqlite3.connect(db_name) as conn:
        df = pd.read_sql_query(query, conn, params=(status, city))
        df["avg_check"] = (df["total_spent"] / df["orders_count"]).round(2)
        df.to_sql("top_customers_report", conn, if_exists="replace", index=False)

        result = pd.read_sql_query("SELECT * FROM top_customers_report", conn)
        print(f"ТОП-5 клієнтів у місті {city} (статус: {status}):")
        print(result.to_string(index=False))


def main() -> None:
    """Запускає усі кроки лабораторної роботи."""
    db_name = "ecommerce.db"
    csv_file = "module1_ecommerce_orders.csv"
    city = "Київ"

    create_database(db_name)
    import_orders(csv_file, db_name)
    make_top_customers_report(db_name, city)


if __name__ == "__main__":
    main()
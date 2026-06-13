import sqlite3
import csv


connection = sqlite3.connect(
    "tickets.db"
)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER,
    category TEXT,
    priority TEXT,
    reason TEXT
)
""")


with open(
    "output/results.csv",
    "r"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute(
            """
            INSERT INTO tickets
            VALUES (?, ?, ?, ?)
            """,
            (
                row["ticket_id"],
                row["category"],
                row["priority"],
                row["reason"]
            )
        )


connection.commit()
connection.close()


print(
    "Data stored in SQLite successfully!"
)
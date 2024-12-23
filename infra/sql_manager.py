import sqlite3
from typing import List, Dict, Any


class SQLManager:
    def __init__(self, db):
        self.db = db

    def insert_many(self, table_name, data):
        if not data:
            print("No data to insert.")
            return 0

        try:
            with sqlite3.connect(self.db) as connection:
                cursor = connection.cursor()

                columns = list(data[0].keys())

                # Create the INSERT query dynamically
                placeholders = ', '.join(['?' for _ in columns])
                column_names = ', '.join(columns)

                query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

                # Prepare the data for bulk insertion
                values = [
                    [row.get(col) for col in columns]
                    for row in data
                ]

                cursor.executemany(query, values)

                connection.commit()
                return cursor.rowcount

        except sqlite3.Error as e:
            print(f"An error occurred during insertion: {e}")
            return None


    def execute_query(self, query):
        try:
            with sqlite3.connect(self.db) as connection:
                cursor = connection.cursor()
                cursor.execute(query)

                results = cursor.fetchall()

                return results

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

#Example usage:
# if __name__ == "__main__":
#     myDB = '/Users/user/deepDB.db'
#     db_helper = SQLManager(db=myDB)
#     results = db_helper.execute_query("SELECT * FROM companies")
#     print(results)
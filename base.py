
import psycopg2 as db
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, type: str):
        database = db.connect(
            database=os.getenv("db_name"),
            host=os.getenv("db_host"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password")
        )

        cursor = database.cursor()
        cursor.execute(query)

        data_type = ["create", "insert", "delete", "update",]
        if type in data_type:
            database.commit()

            if type == "insert":
                return "inserted"

            elif type == "delete":
                return "deleted"

            else:
                return "updated"

        elif type == "select":
            return cursor.fetchall()

        else:
            return "*** Aniqlanmagan query ***"
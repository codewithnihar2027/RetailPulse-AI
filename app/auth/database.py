import sqlite3
from pathlib import Path

DATABASE_DIR = Path("data")
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "users.db"


class AuthDatabase:

    @staticmethod
    def get_connection():
        return sqlite3.connect(DATABASE_PATH)

    @staticmethod
    def initialize():

        conn = AuthDatabase.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    @staticmethod
    def create_user(
        full_name: str,
        email: str,
        password_hash: str
    ) -> bool:

        conn = AuthDatabase.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users
                (full_name, email, password_hash)
                VALUES (?, ?, ?)
                """,
                (full_name, email, password_hash)
            )

            conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False

        finally:
            conn.close()

    @staticmethod
    def get_user_by_email(email: str):

        conn = AuthDatabase.get_connection()
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        return user
    @staticmethod
    def user_exists(email: str) -> bool:

        return (
            AuthDatabase.get_user_by_email(email)
            is not None
        )
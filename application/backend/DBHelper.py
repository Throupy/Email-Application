"""Execure database commands."""
import sqlite3


class DBHelper:
    """Execute database commands."""

    def __init__(self):
        """Initialize the database class."""
        self.connection = sqlite3.connect("application.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                               ID INTEGER PRIMARY KEY,
                               username TEXT,
                               password TEXT)""")

    def userExists(self, username):
        """Check if a user exists."""
        self.cursor.execute("SELECT * FROM users WHERE username = (?)",
                            (username,)
                            )
        rows = self.cursor.fetchone()
        if rows is None:
            return False
        return True

    def createUser(self, username, password):
        """Create a user with the specified information."""
        self.cursor.execute("""INSERT INTO users (username, password)
                               VALUES (?,?)""", (username, password))

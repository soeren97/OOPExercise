"""Create table on SQL server."""

import mysql.connector
from mysql.connector import Error
from mysql.connector.abstracts import MySQLCursorAbstract


class DatabaseCreator:
    """Handle generation of SQL databases and tables."""

    def __init__(self, user: str, password: str, database: str, table: str) -> None:
        """Initialize class.

        Args:
            user (str): Username used for SQL connection.
            password (str): Password used for SQL connection.
            database (str): Database name.
            table (str): Table name.
        """
        self.user = user
        self.password = password
        self.database = database
        self.host = "localhost"
        self.table = table

    def initialize_table(self, cursor: MySQLCursorAbstract) -> None:
        """Create a table if not pressent.

        Args:
            cursor (MySQLCursorAbstract): A MySQL cursor object to execute SQL queries.
            The cursor should be initialized and connected to a database.
        """
        try:
            cursor.execute(f"USE {self.database}")
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {self.table} (
                id BIGINT AUTO_INCREMENT PRIMARY KEY,
                category VARCHAR(255),
                size INT,
                color VARCHAR(255),
                price FLOAT,
                material VARCHAR(255),
                sleeves BOOLEAN,
                style VARCHAR(255),
                length VARCHAR(255)
            )
            """
            cursor.execute(create_table_query)
            print(f"Table '{self.table}' initialized successfully")
        except Error as e:
            print(f"Error initializing table: {e}")
        finally:
            cursor.close()

    def create_database(self) -> None:
        """Create a database if not present."""
        try:
            connection = mysql.connector.connect(
                host=self.host, user=self.user, password=self.password
            )
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.initialize_table(cursor)
            print(f"Database '{self.database}' created successfully")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

"""Connection to SQL database."""

from typing import Any, Optional

import mysql.connector
from mysql.connector import Error
from mysql.connector.abstracts import MySQLConnectionAbstract


class DatabaseConnection:
    """Class to handle connection to SQL database."""

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
        self.table = table
        self.connection: MySQLConnectionAbstract = None
        self.connect()

    _instance = None

    def __new__(cls: Any, *args: tuple[Any], **kwargs: tuple[Any]) -> Any:
        """Make sure there is only one instance of this class.

        Args:
            cls (DatabaseConnection): The class of the instance being created.

        Returns:
            DatabaseConnection: The instance of the DatabaseConnection class.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self) -> None:
        """Connect to the SQL server."""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database=self.database,
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None

    def execute_query(self, query: str) -> Any:
        """Execute a SQL query.

        Args:
            query (str): Query to be executed.

        Returns:
            Any: The response from the query.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            self.connection.commit()
            print("Query executed successfully")
            return result
        except Error as e:
            print(f"Error executing write query: {e}")

    def fetch_item_by_id(self, item_id: str) -> Any:
        """Get a clothing item from ID.

        Args:
            item_id (str): Cloth ID

        Returns:
            Optional[Any]: The requested clothing item.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table} WHERE id = %s"
            cursor.execute(query, (item_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching item by ID: {e}")
            return None

    def fetch_all_data(self) -> Any:
        """Get all data from the table specified in config.json.

        Returns:
            Any: All data from the table.
        """
        return self.execute_query(f"SELECT * FROM {self.table}")

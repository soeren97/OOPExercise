"""The main script."""

from src.clothes.factory import ClothesFactory
from src.database.connection import DatabaseConnection
from src.database.generation import DatabaseCreator
from src.utils import ConfigManager


def main() -> None:
    """Facilitate the main logic."""
    # Load conig
    config = ConfigManager(filepath="config.json")

    # Create database if not pressent.
    creator = DatabaseCreator(
        config.username(),
        config.password(),
        config.database(),
        config.table(),
    )
    creator.create_database()

    # Connect to database
    connection = DatabaseConnection(
        user=config.username(),
        password=config.password(),
        database=config.database(),
        table=config.table(),
    )

    # Create factory to create clothes
    factory = ClothesFactory()

    # Generate query
    query = factory.create_random_clothes().to_sql_query()

    # Write to SQL server
    connection.execute_query(query)

    # Fetch entire database
    result = connection.fetch_all_data()
    print(result)


if __name__ == "__main__":
    main()

"""Clothing items."""

from typing import Any, Optional


class Clothes:
    """Base class for clothing items."""

    def __init__(
        self,
        size: Optional[int] = None,
        color: Optional[str] = None,
        price: Optional[float] = None,
        material: Optional[str] = None,
        id: Optional[int] = None,
        category: Optional[str] = None,
        **kwargs: tuple[Any],
    ) -> None:
        """Initialize the class.

        Args:
            size (int, optional): Size of the clothing. Defaults to None.
            color (str, optional): Color of the clothing. Defaults to None.
            price (float, optional): Price of the clothing. Defaults to None.
            material (str, optional): Material of the clothing. Defaults to None.
            id (int, optional): ID of the clothing. Defaults to None.
            category (str, optional): Category of the clothing item. Defaults to None.
        """
        self.size = size
        self.color = color
        self.price = price
        self.material = material
        self.id = id
        self.category = category
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_sql_query(self) -> str:
        """Convert the clothes into a SQL insert query based on attributes.

        Returns:
            str: SQL insert query.
        """
        attributes = vars(self)
        attribute_names = list(attributes.keys())
        attribute_values = list(attributes.values())

        # Filter out None values and convert others to string if necessary
        attribute_strings = [
            f"'{value}'" if isinstance(value, str) else str(value)
            for value in attribute_values
            if value is not None
        ]

        # Create the SQL query
        query = f"""INSERT INTO Clothes ({', '.join(attribute_names)})
VALUES ({', '.join(attribute_strings)})"""
        return query


class Top(Clothes):
    """Top clothing items."""

    def __init__(
        self,
        size: Optional[int] = None,
        color: Optional[str] = None,
        price: Optional[float] = None,
        sleeves: Optional[bool] = None,
        material: Optional[str] = None,
        id: Optional[int] = None,
    ) -> None:
        """Initialize the class.

        Args:
            size (int, optional): Size of the clothing. Defaults to None.
            color (str, optional): Color of the clothing. Defaults to None.
            price (float, optional): Price of the clothing. Defaults to None.
            sleeves (bool, optional): Does the top have sleves. Defaults to None.
            material (str, optional): Material of the clothing. Defaults to None.
            id (int, optional): ID of the clothing. Defaults to None.
        """
        super().__init__(size, color, price, material, id)
        self.sleeves = sleeves


class Footwear(Clothes):
    """Footware clothing items."""

    def __init__(
        self,
        size: Optional[int] = None,
        color: Optional[str] = None,
        price: Optional[float] = None,
        material: Optional[str] = None,
        id: Optional[int] = None,
    ) -> None:
        """Initialize the class.

        Args:
            size (int, optional): Size of the clothing. Defaults to None.
            color (str, optional): Color of the clothing. Defaults to None.
            price (float, optional): Price of the clothing. Defaults to None.
            material (str, optional): Material of the clothing. Defaults to None.
            id (int, optional): ID of the clothing. Defaults to None.
        """
        super().__init__(size, color, price, material, id)


class Headwear(Clothes):
    """Headwear clothing items."""

    def __init__(
        self,
        size: Optional[int] = None,
        color: Optional[str] = None,
        price: Optional[float] = None,
        style: Optional[str] = None,
        material: Optional[str] = None,
        id: Optional[int] = None,
    ) -> None:
        """Initialize the class.

        Args:
            size (int, optional): Size of the clothing. Defaults to None.
            color (str, optional): Color of the clothing. Defaults to None.
            price (float, optional): Price of the clothing. Defaults to None.
            style (str, optional): Style of the top. Defaults to None.
            material (str, optional): Material of the clothing. Defaults to None.
            id (int, optional): ID of the clothing. Defaults to None.
        """
        super().__init__(size, color, price, material, id)
        self.style = style


class Bottoms(Clothes):
    """Bottem clothing items."""

    def __init__(
        self,
        size: Optional[int] = None,
        color: Optional[str] = None,
        price: Optional[float] = None,
        length: Optional[str] = None,
        material: Optional[str] = None,
        id: Optional[int] = None,
    ) -> None:
        """Initialize the class.

        Args:
            size (int, optional): Size of the clothing. Defaults to None.
            color (str, optional): Color of the clothing. Defaults to None.
            price (float, optional): Price of the clothing. Defaults to None.
            length (str, optional): Length of the clothing. Defaults to None.
            material (str, optional): Material of the clothing. Defaults to None.
            id (int, optional): ID of the clothing. Defaults to None.
        """
        super().__init__(size, color, price, material, id)
        self.length = length

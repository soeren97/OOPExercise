"""Factory of creating clothing."""

import random
import time
from typing import Any

from src.clothes.items import Bottoms, Clothes, Footwear, Headwear, Top


class ClothesFactory:
    """Factory class that creates clothing.

    Raises:
        ValueError: Category not in allowed categories.
    """

    item_id = {
        "Top": 1,
        "Footwear": 2,
        "Headwear": 3,
        "Bottoms": 4,
    }
    item_types = {
        "Top": Top,
        "Footwear": Footwear,
        "Headwear": Headwear,
        "Bottoms": Bottoms,
    }

    @staticmethod
    def create_clothes(category: str, **kwargs: tuple[Any]) -> Any:
        """Create a piece of clothing from category and attributes.

        Args:
            category (str): Type of clothing.

        Raises:
            ValueError: Category not in allowed categories.

        Returns:
            Clothes: Finished clothes.
        """
        if category not in ClothesFactory.item_types:
            raise ValueError(f"Invalid item type: {category}")

        id = ClothesFactory._generate_id(category)

        constructor = ClothesFactory.item_types[category]
        return constructor(id=id, **kwargs)

    @staticmethod
    def _generate_id(category: str) -> int:
        """Generate a unique id for a clothing item.

        Args:
            category (str): Category of the clothing

        Returns:
            str: Id of the clothing item.
        """
        return int(f"{ClothesFactory.item_id[category]}{int(time.perf_counter_ns())}")

    def create_random_clothes(self) -> Clothes:
        """Create a random piece of clothing.

        Can be used to fill up an empty server for testing purposes.

        Returns:
            Clothes: Random clothing item.
        """
        category = random.choice(["Top", "Footwear", "Headwear", "Bottoms"])
        size = random.randint(30, 50)
        color = random.choice(["Red", "Blue", "Green", "Black", "White"])
        price = round(random.uniform(10.0, 100.0), 2)
        material = random.choice(["Cotton", "Leather", "Wool", "Denim"])

        clothes = Clothes(
            id=ClothesFactory._generate_id(category),
            category=category,
            size=size,
            color=color,
            price=price,
            material=material,
        )

        if category == "Top":
            sleeves = random.choice([True, False])
            clothes.sleeves = sleeves  # type: ignore [attr-defined]
        elif category == "Headwear":
            style = random.choice(["Cap", "Hat", "Beanie"])
            clothes.style = style  # type: ignore [attr-defined]
        elif category == "Bottoms":
            length = random.choice(["Short", "Medium", "Long"])
            clothes.length = length  # type: ignore [attr-defined]

        return clothes

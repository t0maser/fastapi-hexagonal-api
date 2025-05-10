# This module contains the application services (use cases).

from ..domain.entities import Item

def get_item_details(name: str) -> Item:
    # Simulate fetching item details
    return Item(name=name, description=f"Description for {name}")
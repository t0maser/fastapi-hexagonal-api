# This module contains the core business entities for the application.

class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Item(name={self.name}, description={self.description})"
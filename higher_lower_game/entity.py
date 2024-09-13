"""
    1. entity maps to json data structure
"""


class ComparedItem:
    def __init__(self, name, follower_count, description, country):
        self.name = name
        self.follower_count = follower_count
        self.description = description
        self.country = country

    def __str__(self):
        return f'{self.name}, {self.follower_count}, {self.description}, {self.country}'

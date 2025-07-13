"""
Define programming language class
Goaltime: 10 min
Worktime: 6 min
Code by: Miss Ghost/April First
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage instance."""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'

    def is_dynamic(self):
        """Return True if the programming language is dynamic."""
        return "Dynamic" in self.typing

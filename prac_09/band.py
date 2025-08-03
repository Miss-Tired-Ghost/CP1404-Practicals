"""
Association implementation
Code By: April First/Miss Ghost
"""


class Band:
    """Band class"""
    def __init__(self, name=""):
        """Construct an empty band with given name"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band"""
        representation = f"{self.name}("
        for musician in self.musicians:
            representation += f"{musician},"
        representation = f"{representation[:-1]})"
        return representation

    def add(self, musician):
        """Add musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string of each musician in the band and which instrument they are playing"""
        playing = f""
        for musician in self.musicians:
            playing += f"{musician.play()}\n"
        playing = f"{playing[:-1]})"
        return playing

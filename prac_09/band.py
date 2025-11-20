class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def play(self):
        for musician in self.musicians:
            print(musician.play())
        return

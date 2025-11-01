"""
Estimated = 35 mins
Actual =
"""

vintage = 50
present_year = 2025

class Guitar:
    def __int__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return present_year - self.year

    def is_vintage(self):
        return self.get_age() >= vintage

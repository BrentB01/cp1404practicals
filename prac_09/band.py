class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        musicians_str = ', '.join(str(m) for m in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        for musician in self.musicians:
            print(musician.play())






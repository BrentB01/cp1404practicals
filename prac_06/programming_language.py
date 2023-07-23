class ProgrammingLanguage:

    def __init__(self, name, typing_style, reflection, year):
        self.name = name
        self.typing_style = typing_style
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing_style == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing_style}, Reflection={self.reflection}, First appeared in {self.year}"


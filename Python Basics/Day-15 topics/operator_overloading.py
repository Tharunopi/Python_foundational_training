class Name:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}"

name = Name("Tharun")
print(name)
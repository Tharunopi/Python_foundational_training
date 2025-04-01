class Parent_1:
    def __init__(self, name_1):
        self.name_1 = name_1

    def display_1(self):
        print(self.name_1)

class Parent_2:
    def __init__(self, name):
        self.name = name

    def display_2(self):
        print(self.name)

class Child_1(Parent_1, Parent_2):
    def __init__(self, name_1, name_2, name_3):
        Parent_1.__init__(self, name_1)
        Parent_2.__init__(self, name_2)
        self.name_3 = name_3

    def display_3(self):
        print(self.name_3)

child = Child_1("Parent-1", "Parent-2", "Child-1")
child.display_1()
child.display_2()
child.display_3()
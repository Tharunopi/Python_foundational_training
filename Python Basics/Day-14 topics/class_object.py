class one:
    __name = "Tharun" #private variable
    _name = "Tharun" #protected variable
    name = "Tharun" #public variable
    def func_1(self):
        print("Hello, World")

    def func_2(self, place):
        print(f"loc: {place}")

# object
a = one()
a.func_1()
a.func_2("Kgm")
print(a.name)
print(a._name)
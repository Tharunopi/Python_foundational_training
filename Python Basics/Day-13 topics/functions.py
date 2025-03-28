# functions 
def greet(name):
    """Pass your name to get greetings."""
    return print(f"Hello! {name}, How are you?")

types_of_func = """User defined functions
    1. func with parameters with return value
    2. func with parameters without return value
    3. func without parameters with return value
    4. func without parameters without return value"""

# 1. func with parameters with return value
def add(a:int, b:int) -> int:
    return a + b

# 2. func with parameters without return value
def display(x):
    print(x)

# 3. func without parameters with return value
def pi():
    return 3.14

# 4. func without parameters without return value
def update_db():
    # imagine updated your login time in database
    print("updated")

print(add(2, 3))
display(499303)
print(pi())
update_db()
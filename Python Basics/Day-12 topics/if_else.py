# if statement
a = 50
b = 100
c = 200

if a == 5:
    print("a = b")
else:
    print("a != b")

# nested if-else statement
if a < b:
    if c > b:
        print("c is greater")
    else:
        print("b is greater")
else:
    print("a is greater")

# elif statement

if a == 100:
    print("a = 100")
elif b == 100:
    print("b = 100")
else:
    print("c = 100")

# checking odd or even 
x = 10

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
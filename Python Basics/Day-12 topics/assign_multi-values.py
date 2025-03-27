# assigning single values to multiple variables
a = b = c = 40
print(a, b, c)

# assigning multiple values to multiple variables
x, y, z = 10, 20, 30
print(x, y, z)

# task
a, b = int(input("Enter num-1: ")), int(input("Enter num-2: "))
print(f"a- {a}, b- {b}")

# swapping without using temp-var
a, b = b, a
print(f"a- {a}, b- {b}")

# swapping using temp-var
c = a
a = b
b = c
print(f"a- {a}, b- {b}")
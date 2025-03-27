# string declaration

a = 'string'
b = "string"
c = """string
.
.
"""

print(a)
print(b)
print(c)

# string concatenation

print(a + b)

# string multiplication

print(a * 5)

# join 
print("-".join(a))

# upper, lower
print(a.upper(), a.lower())

# strip, replace, split
print(a.split(" "))
print(a.strip())
print(a.replace('s', 'S'))

# min, max
print(min(a))
print(max(a))
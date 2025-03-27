# for loop
words = ["mac", "linux", "windows"]

for i in words:
    print(i)

# printing multiplication table 
table = 9

for i in range(10):
    print(f"{i+1} * {table} = {(i + 1) * table}")


# while loop
a = 0
stat = True
while stat:
    print(a)
    if a > 5:
        stat = False
    a += 1
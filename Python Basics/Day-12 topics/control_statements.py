# break statement

value = "Python"

for i in value:
    if i == "t":
        break
    print("Not found") 

i = 1 
sum = 0

while i <= 5:
    num = int(input(f"Enter sub-{i} marks: "))
    if num < 0:
        print("Unable to process negative value")
        break
    sum += num
    i += 1 

print(sum)

# continue statement
for i in value:
    if i == "t":
        continue
    print(i) 

# pass statement
for f in "aids":
    pass
print(f)
num = [1, 2, 3, 4, 5]

print(num)

for i in num:
    print(i)

print(["oh"] + [1, 2, 3] + ["Tharun"])

num.reverse()
print(num)

# deep copy
list_1 = [10, 20, 30]
list_2 = list_1
list_2.pop(2)
print(list_1, list_2)

list_10 = [10, 20, 30]
list_20 = list_10.copy()
list_20.pop(2)
print(list_10, list_20)
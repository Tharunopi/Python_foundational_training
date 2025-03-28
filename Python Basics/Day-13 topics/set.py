name_set = {"vino", "raj", "abi", "kumar", 1, 1}

name_set.add("one piece")
name_set.remove("one piece")

mark1 = {1, 2, 3, 4}
mark2 = {4, 5, 6, 7}

un = mark1.union(mark2)
print(un)

print(mark1.intersection(mark2))

print(mark1.difference(mark2))

print(mark1.symmetric_difference(mark2))
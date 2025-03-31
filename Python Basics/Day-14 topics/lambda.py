c = lambda a, b: int(a * b * 10)

print(c(10, 20))

# 4 asynchronous function: map, filter, reduce, sorted
# map()
salary = [100, 2000, 5000, 3423]
inc_ = list(map(lambda x: x+100, salary))
print(inc_)

# filter()
res_filter = list(filter(lambda x: (x%2 != 0), salary))
print(res_filter)

# reduce()
from functools import reduce
res_reduce = reduce(lambda x, y: x + y, salary)
print(res_reduce)

# sorted()
values = [[10, 1], [50, 5], [20, 2]]
sor_values = sorted(values, key=lambda x:x[1], reverse=True)
print(sor_values)
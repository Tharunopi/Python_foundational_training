a = [1, 2, 3]
try:
    print(a[10])

except IndexError:
    raise IndexError("Check the Index")

except TypeError:
    raise TypeError("Check type")

except Exception as e:
    print(e)
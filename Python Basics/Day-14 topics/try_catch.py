try:
    c = 10/0
except:
    print(ZeroDivisionError)
finally:
    print("Done")
class One:
    def sum(self, a, b):
        print(a + b)

class Two(One):
    def sum(self, a, b, c):
        print(a + b + c)
        
cal = One()
caal = Two()
cal.sum(1, 2)
caal.sum(1, 2, 3)
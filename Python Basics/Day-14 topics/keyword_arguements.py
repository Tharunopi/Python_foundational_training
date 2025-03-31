def addittion(*args):
    values = list(filter(lambda x: x>= 15 ,args))
    print(values)

def subraction(**kwargs):
    values = lambda x: x["topic"] if x["topic"] == 'Bleach' else 'one piece'
    print(values(kwargs))

def test(*args, **kwargs):
    print(args, kwargs)

test(1, 2, 3, name="Alice", age=25)
addittion(10, 20, 30, 40)
subraction(anime=True, topic="Bleach")
from bs4 import BeautifulSoup
import lxml

path = r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\basic-structure.xml"

with open(path, 'r') as f:
    data = f.read()

bs = BeautifulSoup(data, features="xml")
print(bs)
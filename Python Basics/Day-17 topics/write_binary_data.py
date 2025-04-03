data = b'\x12'
with open(r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\binary image data.jpg", 'wb+') as f:
    f.write(data)
    print(f.read())
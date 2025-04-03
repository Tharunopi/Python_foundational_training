with open(r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\bleach.jpg", 'rb') as f:
    with open(r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\bleach_copy.jpg", 'wb') as b:
        b.write(f.read())
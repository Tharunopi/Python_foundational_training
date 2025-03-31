# Write a Python program to sort a list of tuples using Lambda.
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_subjects = sorted(subjects, key=lambda x: x[1])
print(sorted_subjects)
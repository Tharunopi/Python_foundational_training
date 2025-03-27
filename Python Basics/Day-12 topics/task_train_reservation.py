# train reservation 

total_price = 0
no_of_tickets = int(input("Enter of tickets: "))
passengers = []

for i in range(no_of_tickets):
    t_price = 100
    name = input(f"Enter passenger {i+1} name: ")
    gender = input(f"Enter passenger {i+1} gender: ")
    age = int(input(f"Enter passenger {i+1} age: "))
    handicapped = input(f"if handicap y else n: ")

    if handicapped == 'y':
        t_price *= 0
    elif age > 70:
        t_price *= 0.10
    elif gender == 'f' and age >= 50:
        t_price *= 0.50
    elif gender == 'm' and age >= 65:
        t_price *= 0.50
    elif age <= 5:
        t_price *= 0

    gst= t_price * 0.18

    passengers.append(f"Name: {name}, Age: {age}, Gender: {gender.upper()}, ticket price: {t_price} + GST: {gst}")

    t_price += gst
    total_price += t_price

for i in passengers:
    print(i)
print(f"Total payable price: ₹{total_price}/-")
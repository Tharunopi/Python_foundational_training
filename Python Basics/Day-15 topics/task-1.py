class Flight:
    fights = []
    def __init__(self):
        pass

    def add_flight(self, fid, fname, source, destination, ticket_price):
        self.fights.append([fid, fname, source, destination, ticket_price] )
        print("------------------------------------------------")
        print(f"Flight ID: {fid}")
        print(f"Flight Name: {fname}")
        print(f"path: {source} -> {destination}")
        print(f"Ticket Price: {ticket_price}")
        print("------------------------------------------------")

class Customer(Flight):
    customers = []
    def __init__(self):
        pass

    def add_customer(self, cid, cname, address, phone_no):
        self.customers.append([cid, cname, address, phone_no])
        print("------------------------------------------------")
        print(f"Customer ID: {cid}")
        print(f"Customer Name: {cname}")
        print(f"Address: {address}")
        print(f"PhoneNumber: {phone_no}")
        print("------------------------------------------------")

class Booking(Customer):
    booking_history = []
    def __init__(self):
        pass

    def ticket_booking(self, bid, fid, cid, num_tickets, gst):
        flight_details = None
        for i in self.fights:
            if i[0] == fid:
                flight_details = i
                break 

        if flight_details is None:
            return print("Invalid flight details")
        
        ages = []
        ticket_price = []
        deductions = []

        print(f"\t Booking - {bid}")

        for i in range(num_tickets):
            age_ = int(input(f"Enter age of Passenger-{i+1}: "))
            if age_ < 2:
                ticket_price.append(0)
                deductions.append(flight_details[-1])
            elif age_ > 60:
                d_price = flight_details[-1] * 0.40
                ticket_price.append(flight_details[-1] - (d_price))
                deductions.append(d_price)
            else:
                ticket_price.append(flight_details[-1])
                deductions.append(0)
            ages.append(age_)
        
        total_price = sum(ticket_price)
        d_gst = total_price * (gst / 100)
        total_price += d_gst
        deductions.append(d_gst)

        if num_tickets >= 5:
            d_10 = total_price * 0.10
            total_price -= d_10
            deductions.append(d_10)

        saved_amount = sum(deductions)
        self.booking_history.append([bid, fid, cid, num_tickets, gst, total_price, saved_amount])
        
        print("------------------------------------------------")
        print(f"Booking ID: {bid}")
        print(f"Flight ID: {fid}")
        print(f"Customer ID: {cid}")
        print(f"Number of tickets: {num_tickets}")
        print(f"GST : {gst}%")
        print(f"Deductions: ₹{saved_amount}/-")
        print(f"Grand total: ₹{total_price}/-")
        print("------------------------------------------------")

cus = Booking()
cus.add_customer(1, "Tharun", "fffii", "73737373")
cus.add_customer(2, "Atithya", "fkeeke", "84930922")

cus.add_flight(1, "Air India", "India", "USA", 85000)
cus.add_flight(2, "Indigo", "India", "Japan", 45000)
cus.add_flight(3, "KingFisher", "India", "England", 60000)
cus.add_flight(4, "Deccan Flights", "India", "Russia", 40000)

cus.ticket_booking(1, 1, 1, 2, 18)
cus.ticket_booking(2, 4, 2, 1, 18)
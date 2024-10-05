# A class to represent a room in the hotel
class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

# A class to represent a reservation
class Reservation:
    def __init__(self, customer_name, room):
        self.customer_name = customer_name
        self.room = room

# A class to represent the hotel system
class HotelReservationSystem:
    def __init__(self):
        self.rooms = []  # List to store all hotel rooms
        self.reservations = []  # List to store all reservations
    
    # Method to add rooms to the system
    def add_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
    
    # Method to display available rooms
    def display_available_rooms(self):
        print("\nAvailable Rooms:")
        available_rooms = [room for room in self.rooms if room.is_available]
        if not available_rooms:
            print("No rooms available!")
        for room in available_rooms:
            print(f"Room {room.room_number} - Type: {room.room_type} - Price: ${room.price}")
    
    # Method to make a reservation
    def make_reservation(self, customer_name, room_number):
        room = self.find_room(room_number)
        if room and room.is_available:
            reservation = Reservation(customer_name, room)
            self.reservations.append(reservation)
            room.is_available = False
            print(f"\nReservation successful for {customer_name} in Room {room_number}!")
        else:
            print(f"\nRoom {room_number} is not available for booking.")
    
    # Method to cancel a reservation
    def cancel_reservation(self, customer_name, room_number):
        reservation = self.find_reservation(customer_name, room_number)
        if reservation:
            reservation.room.is_available = True
            self.reservations.remove(reservation)
            print(f"\nReservation for {customer_name} in Room {room_number} has been canceled.")
        else:
            print(f"\nNo reservation found for {customer_name} in Room {room_number}.")
    
    # Method to display all reservations
    def display_reservations(self):
        print("\nCurrent Reservations:")
        if not self.reservations:
            print("No reservations found!")
        for reservation in self.reservations:
            print(f"Customer: {reservation.customer_name}, Room: {reservation.room.room_number}")
    
    # Helper method to find a room by room number
    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    # Helper method to find a reservation by customer name and room number
    def find_reservation(self, customer_name, room_number):
        for reservation in self.reservations:
            if reservation.customer_name == customer_name and reservation.room.room_number == room_number:
                return reservation
        return None

# Function to display the menu and handle user input
def display_menu():
    print("\nHotel Reservation System")
    print("1. Display Available Rooms")
    print("2. Make a Reservation")
    print("3. Cancel a Reservation")
    print("4. View Reservations")
    print("5. Exit")

def main():
    # Create the hotel reservation system
    system = HotelReservationSystem()
    
    # Add some rooms to the system
    system.add_room(101, "Single", 100)
    system.add_room(102, "Double", 150)
    system.add_room(103, "Suite", 300)
    
    while True:
        display_menu()
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            system.display_available_rooms()
        elif choice == '2':
            customer_name = input("Enter your name: ")
            room_number = int(input("Enter room number to reserve: "))
            system.make_reservation(customer_name, room_number)
        elif choice == '3':
            customer_name = input("Enter your name: ")
            room_number = int(input("Enter room number to cancel: "))
            system.cancel_reservation(customer_name, room_number)
        elif choice == '4':
            system.display_reservations()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

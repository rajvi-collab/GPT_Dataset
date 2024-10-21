class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)

    def display_available_rooms(self):
        print(f"\nAvailable rooms in {self.name}:")
        available_rooms = [room for room in self.rooms if room.is_available]
        if available_rooms:
            for room in available_rooms:
                print(f"Room {room.room_number}: {room.room_type}, ${room.price_per_night} per night")
        else:
            print("No rooms available at the moment.")

    def make_reservation(self, room_number, guest_name, nights):
        room = self.find_room(room_number)
        if room and room.is_available:
            total_cost = room.price_per_night * nights
            room.is_available = False
            self.reservations[room_number] = {
                'guest_name': guest_name,
                'nights': nights,
                'total_cost': total_cost
            }
            print(f"\nReservation successful! Room {room_number} has been booked by {guest_name} for {nights} nights. Total cost: ${total_cost}")
        else:
            print(f"\nRoom {room_number} is either unavailable or does not exist.")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def cancel_reservation(self, room_number):
        if room_number in self.reservations:
            room = self.find_room(room_number)
            room.is_available = True
            del self.reservations[room_number]
            print(f"\nReservation for room {room_number} has been successfully cancelled.")
        else:
            print(f"\nNo reservation found for room {room_number}.")

    def display_reservations(self):
        print("\nCurrent reservations:")
        if self.reservations:
            for room_number, details in self.reservations.items():
                print(f"Room {room_number}: Reserved by {details['guest_name']} for {details['nights']} nights. Total cost: ${details['total_cost']}")
        else:
            print("No reservations made.")

# Sample usage
def main():
    hotel = Hotel("Oceanview Hotel")

    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 250))

    while True:
        print("\n1. Display available rooms")
        print("2. Make a reservation")
        print("3. Cancel a reservation")
        print("4. View all reservations")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            hotel.display_available_rooms()
        elif choice == '2':
            guest_name = input("Enter guest name: ")
            room_number = int(input("Enter room number to reserve: "))
            nights = int(input("Enter number of nights: "))
            hotel.make_reservation(room_number, guest_name, nights)
        elif choice == '3':
            room_number = int(input("Enter room number to cancel reservation: "))
            hotel.cancel_reservation(room_number)
        elif choice == '4':
            hotel.display_reservations()
        elif choice == '5':
            print("Thank you for using the hotel reservation system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

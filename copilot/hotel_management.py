class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self, room_type):
        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.is_available]
        return available_rooms

    def make_reservation(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                room.is_available = False
                return f"Room {room_number} has been reserved."
        return "Room not available."

    def cancel_reservation(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_available:
                room.is_available = True
                return f"Reservation for room {room_number} has been cancelled."
        return "Room is already available."

def main():
    hotel = Hotel("Grand Hotel")

    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single"))
    hotel.add_room(Room(102, "Double"))
    hotel.add_room(Room(103, "Suite"))

    while True:
        print("\nWelcome to the Grand Hotel Reservation System")
        print("1. Check room availability")
        print("2. Make a reservation")
        print("3. Cancel a reservation")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            room_type = input("Enter room type (Single/Double/Suite): ")
            available_rooms = hotel.check_availability(room_type)
            if available_rooms:
                print(f"Available {room_type} rooms: {[room.room_number for room in available_rooms]}")
            else:
                print(f"No available {room_type} rooms.")
        elif choice == '2':
            room_number = int(input("Enter room number to reserve: "))
            print(hotel.make_reservation(room_number))
        elif choice == '3':
            room_number = int(input("Enter room number to cancel reservation: "))
            print(hotel.cancel_reservation(room_number))
        elif choice == '4':
            print("Thank you for using the Grand Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

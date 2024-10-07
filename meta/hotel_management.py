import datetime

class Room:
    """Represents a hotel room."""

    def __init__(self, room_number, room_type, capacity, price):
        """
        Initializes a Room object.

        Args:
            room_number (int): Unique room number.
            room_type (str): Type of room (e.g., Single, Double, Suite).
            capacity (int): Maximum number of guests.
            price (float): Room price per night.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = capacity
        self.price = price
        self.is_reserved = False


class Hotel:
    """Manages hotel rooms and reservations."""

    def __init__(self, name):
        """
        Initializes a Hotel object.

        Args:
            name (str): Hotel name.
        """
        self.name = name
        self.rooms = []

    def add_room(self, room):
        """Adds a room to the hotel."""
        self.rooms.append(room)

    def display_rooms(self):
        """Displays available rooms."""
        print("Available Rooms:")
        for room in self.rooms:
            if not room.is_reserved:
                print(f"Room Number: {room.room_number}, Type: {room.room_type}, Capacity: {room.capacity}, Price: ${room.price}")

    def reserve_room(self, room_number, check_in, check_out, guests):
        """
        Reserves a room.

        Args:
            room_number (int): Room number to reserve.
            check_in (datetime.date): Check-in date.
            check_out (datetime.date): Check-out date.
            guests (int): Number of guests.

        Returns:
            bool: True if reservation is successful, False otherwise.
        """
        for room in self.rooms:
            if room.room_number == room_number and not room.is_reserved:
                if guests <= room.capacity:
                    room.is_reserved = True
                    print(f"Room {room_number} reserved successfully.")
                    print(f"Check-in: {check_in}, Check-out: {check_out}, Guests: {guests}")
                    return True
                else:
                    print("Room capacity exceeded.")
                    return False
        print("Room not available.")
        return False

    def cancel_reservation(self, room_number):
        """
        Cancels a reservation.

        Args:
            room_number (int): Room number to cancel.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        for room in self.rooms:
            if room.room_number == room_number and room.is_reserved:
                room.is_reserved = False
                print(f"Reservation for Room {room_number} cancelled.")
                return True
        print("Room not reserved.")
        return False


def main():
    # Create a hotel
    hotel = Hotel("Grand Plaza")

    # Add rooms
    hotel.add_room(Room(101, "Single", 1, 100.0))
    hotel.add_room(Room(102, "Double", 2, 150.0))
    hotel.add_room(Room(103, "Suite", 4, 300.0))

    while True:
        print("\nHotel Reservation System")
        print("1. Display Available Rooms")
        print("2. Reserve Room")
        print("3. Cancel Reservation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.display_rooms()
        elif choice == "2":
            room_number = int(input("Enter room number: "))
            check_in = datetime.datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            check_out = datetime.datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            guests = int(input("Enter number of guests: "))
            hotel.reserve_room(room_number, check_in, check_out, guests)
        elif choice == "3":
            room_number = int(input("Enter room number: "))
            hotel.cancel_reservation(room_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
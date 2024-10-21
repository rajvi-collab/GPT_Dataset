class HotelReservationSystem:
    def __init__(self):
        self.rooms = {
            "101": {"type": "Single", "status": "Available"},
            "102": {"type": "Double", "status": "Available"},
            "103": {"type": "Suite", "status": "Available"},
            # Add more rooms as needed
        }
        self.reservations = {}

    def display_rooms(self):
        """Display available rooms"""
        print("Available Rooms:")
        for room, details in self.rooms.items():
            if details["status"] == "Available":
                print(f"Room {room}: {details['type']}")

    def book_room(self, room_number, guest_name, arrival_date, departure_date):
        """Book a room"""
        if self.rooms[room_number]["status"] == "Available":
            self.rooms[room_number]["status"] = "Booked"
            self.reservations[room_number] = {
                "guest_name": guest_name,
                "arrival_date": arrival_date,
                "departure_date": departure_date,
            }
            print(f"Room {room_number} booked successfully for {guest_name}.")
        else:
            print(f"Room {room_number} is not available.")

    def cancel_reservation(self, room_number):
        """Cancel a reservation"""
        if self.rooms[room_number]["status"] == "Booked":
            self.rooms[room_number]["status"] = "Available"
            del self.reservations[room_number]
            print(f"Reservation for room {room_number} cancelled.")
        else:
            print(f"Room {room_number} is not booked.")

    def view_reservations(self):
        """View all reservations"""
        print("Current Reservations:")
        for room, details in self.reservations.items():
            print(f"Room {room}:")
            print(f"Guest Name: {details['guest_name']}")
            print(f"Arrival Date: {details['arrival_date']}")
            print(f"Departure Date: {details['departure_date']}\n")


def main():
    hotel_system = HotelReservationSystem()

    while True:
        print("Hotel Reservation System")
        print("1. Display Available Rooms")
        print("2. Book Room")
        print("3. Cancel Reservation")
        print("4. View Reservations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel_system.display_rooms()
        elif choice == "2":
            room_number = input("Enter room number: ")
            guest_name = input("Enter guest name: ")
            arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            hotel_system.book_room(room_number, guest_name, arrival_date, departure_date)
        elif choice == "3":
            room_number = input("Enter room number: ")
            hotel_system.cancel_reservation(room_number)
        elif choice == "4":
            hotel_system.view_reservations()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
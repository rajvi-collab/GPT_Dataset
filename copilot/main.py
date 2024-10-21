from rooms import Room
from reservations import Reservation

def display_rooms(rooms):
    for room in rooms:
        print(room)

def find_room(rooms, room_id):
    for room in rooms:
        if room.room_id == room_id:
            return room
    return None

def make_reservation(rooms, reservations):
    room_id = int(input("Enter room ID to book: "))
    room = find_room(rooms, room_id)
    if room and room.available:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        reservation = Reservation(room, name, email, date)
        reservations.append(reservation)
        room.available = False
        print("Reservation successful!")
    else:
        print("Room not available or invalid room ID.")

def main():
    rooms = [
        Room(101, 'Single', 100),
        Room(102, 'Double', 150),
        Room(103, 'Suite', 200)
    ]
    reservations = []

    while True:
        print("\n1. View Rooms\n2. Make a Reservation\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_rooms(rooms)
        elif choice == '2':
            make_reservation(rooms, reservations)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

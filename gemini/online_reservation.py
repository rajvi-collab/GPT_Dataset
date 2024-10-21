import datetime

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

class Room:
    def __init__(self, number, capacity, rate):
        self.number = number
        self.capacity = capacity
        self.rate = rate
        self.availability = True

class Reservation:
    def __init__(self, guest_name, room, check_in, check_out):
        self.guest_name = guest_name
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

class ReservationSystem:
    def __init__(self, hotel):
        self.hotel = hotel
        self.reservations = []
        

def check_availability(self, check_in, check_out):
    available_rooms = []
    for room in self.hotel.rooms:
        if room.availability:
            if not any(res.room == room and (check_in >= res.check_in and check_in < res.check_out)
                       or (check_out > res.check_in and check_out <= res.check_out)):
                available_rooms.append(room)
    return available_rooms

    def make_reservation(self, guest_name, room_number, check_in, check_out):
        room = None
        for room in self.hotel.rooms:
            if room.number == room_number:
                break
        if room and room.availability:
            reservation = Reservation(guest_name, room, check_in, check_out)
            self.reservations.append(reservation)
            room.availability = False
            return reservation
        else:
            return None

    def cancel_reservation(self, reservation_id):
        reservation = None
        for res in self.reservations:
            if res.id == reservation_id:
                reservation = res
                break
        if reservation:
            self.reservations.remove(reservation)
            reservation.room.availability = True
            return True
        else:
            return False

# Example usage:
hotel = Hotel("Grand Hotel", [
    Room(1, 2, 100),
    Room(2, 4, 150),
    Room(3, 2, 100)
])

reservation_system = ReservationSystem(hotel)

# Check availability
available_rooms = reservation_system.check_availability(datetime.date(2024, 10, 1), datetime.date(2024, 10, 5))
print("Available rooms:")
for room in available_rooms:
    print(f"Room {room.number} (capacity {room.capacity}, rate {room.rate})")

# Make a reservation
reservation = reservation_system.make_reservation("John Doe", 1, datetime.date(2024, 10, 1), datetime.date(2024, 10, 3))
if reservation:
    print("Reservation made successfully.")
else:
    print("Reservation failed.")

# Cancel a reservation
reservation_system.cancel_reservation(reservation.id)


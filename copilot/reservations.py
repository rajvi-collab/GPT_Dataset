class Reservation:
    def __init__(self, room, name, email, date):
        self.room = room
        self.name = name
        self.email = email
        self.date = date

    def __str__(self):
        return f"Reservation for {self.name} in Room {self.room.room_id} on {self.date}"

class Room:
    def __init__(self, room_id, room_type, price, available=True):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.available = available

    def __str__(self):
        return f"Room {self.room_id} - {self.room_type} - ${self.price} - {'Available' if self.available else 'Not Available'}"

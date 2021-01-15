class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []

    def add_guest(self, guest):
        self.guest_list.append(guest)
    
    def remove_guest(self, guest):
        self.guest_list.remove(guest)

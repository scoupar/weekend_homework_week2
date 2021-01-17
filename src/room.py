class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.play_list =[]
        self.entry_fee = entry_fee
        self.till = 0

    def add_guest(self, guest):
        if len(self.guest_list) < self.capacity: 
            self.guest_list.append(guest)
        elif len(self.guest_list) >= self.capacity:
            return "Room is full"
    
    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.play_list.append(song)
    
    def accept_fee(self):
        self.till + self.entry_fee
    
    

    
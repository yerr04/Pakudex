class Pakudex:

    # Initializes this object to contain exactly capacity objects when completely full. The default capacity for the pakudex should be 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    # Returns the number of critters currently being stored in the pakudex
    def get_size(self):

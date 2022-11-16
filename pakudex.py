from pakuri import Pakuri

class Pakudex:

    # Initializes this object to contain exactly capacity objects when completely full. The default capacity for the
    # pakudex should be 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    # Returns the number of critters currently being stored in the pakudex
    def get_size(self):
        return len(self.pakuri_list)

    # Returns the capacity of the pakudex
    def get_capacity(self):
        return self.capacity

    # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no species
    # added yet, this method should return None
    def get_species_array(self):
        if len(self.pakuri_list) == 0:
            return None
        else:
            species_list = []
            for i in self.pakuri_list:
                species_list.append(i.get_species())
            return species_list

    # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
    # respectively; if species is not in the pakudex, returns None
    def get_stats(self, species):
        for i in self.pakuri_list:
            if i.get_species() == species:
                stat_list = []
                stat_list.append(i.get_attack())
                stat_list.append(i.get_defense())
                stat_list.append(i.get_speed())
                return stat_list
        return None

    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda x: x.get_species())

    def add_pakuri(self, species):
        if len(self.pakuri_list) < self.capacity:
            for i in self.pakuri_list:
                if i.get_species() == species:
                    print("Error: Pakudex already contains this species!")
                    return False
            self.pakuri_list.append(Pakuri(species))
            return True
        else:
            return False

        # Attempts to evolve a specific species within the pakudex; if successful, return True, and False otherwise
    def evolve_species(self, species):
        for i in self.pakuri_list:
            if i.get_species() == species:
                i.evolve()
                return True
        return False



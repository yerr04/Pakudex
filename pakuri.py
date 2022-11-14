class Pakuri:

    # initialize the pakuri object with species attribute
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # returns the species
    def get_species(self):
        return self.species

    # returns the attack
    def get_attack(self):
        return self.attack

    # returns the defense
    def get_defense(self):
        return self.defense

    # returns the speed
    def get_speed(self):
        return self.speed

    # Changes the attack value for this critter to new_attack
    def set_attack(self, new_attack):
        self.attack = new_attack

    # Will evolve the pakuri as follows: double the attack, quadruple the defense, and triple the speed
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

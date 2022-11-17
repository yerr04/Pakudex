from pakudex import Pakudex


def main_menu():  # Displays the main menu and returns the user's choice
    print("Pakudex Main Menu")
    print("-" * 17)
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit \n")
    menu = input("What would you like to do? ")
    return menu


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    program = True
    while program:
        max_capacity = input("Enter max capacity of the Pakudex: ")
        while max_capacity.isdigit() is False or int(max_capacity) < 1:
            print("Please enter a valid size.")
            max_capacity = input("Enter max capacity of the Pakudex: ")
        max_capacity = int(max_capacity)
        print("The Pakudex can hold {} species of Pakuri.".format(max_capacity))
        dex = Pakudex(max_capacity)
        choice = main_menu()
        while choice:
            try:
                choice = int(choice)
            except ValueError:
                print("Unrecognized menu selection!")
            if choice == 1:
                if dex.get_species_array() is None:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri In Pakudex: ")
                    for i in range(0, dex.get_size()):
                        print(str(i + 1) + ". " + dex.get_species_array()[i])

            elif choice == 2:
                species = input("Enter the name of the species to display: ")

                species_stats = dex.get_stats(species)
                if species_stats is None:
                    print("Error: No such Pakuri!")
                else:
                    print("Species: {}".format(species))
                    print("Attack: {}".format(species_stats[0]))
                    print("Defense: {}".format(species_stats[1]))
                    print("Speed: {}".format(species_stats[2]))

            elif choice == 3:

                if dex.get_size() == max_capacity:
                    print("Error: Pakudex is full!")
                else:
                    species = input("Enter the name of the species to add: ")
                    dex.add_pakuri(species)


            elif choice == 4:
                try:
                    species = input("Enter the name of the species to evolve: ")
                    if dex.evolve_species(species):
                        print(species + " has evolved!")
                    else:
                        print("Error: No such Pakuri!")
                except:
                    print("Error: No such Pakuri!")

            elif choice == 5:
                dex.sort_pakuri()
                print("Pakuri have been sorted!")
            elif choice == 6:
                print("Thanks for using Pakudex! Bye!")
                program = False
                break
            else:
                try:
                    if int(choice) > 6 or int(choice) < 1:
                        print("Unrecognized menu selection!")
                except ValueError:
                    print("")
            choice = main_menu()



if __name__ == "__main__":
    main()

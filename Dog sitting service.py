def dropOff():
    input_name = input("Enter the name of the dog: ")
    roll.append(input_name)


def pickUp():
    input_name = input("Enter the name of the dog that you want to pick up")
    if input_name in roll:
        roll.remove(input_name)
        print(f"The dog {input_name} has been removed from the list.")
    else:
        print(f"We cannot find dog name with {input_name}")

def calcCost():
    rate = 22.50
    number_of_dogs = int(input("How many dogs are you picking up: "))
    days_past = int(input("How many days past drop off a dog: "))
    total = number_of_dogs * days_past * rate
    print(f"The total of {number_of_dogs} of dogs for {days_past} days is ${total}")

def printRoll():
    print("Dogs currently staying with DogsRus: ")
    for dog in roll:
        print(f"\t {dog}")
    print()


roll = []

choice = 0

# Main routine
while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to DogsRus")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a dog")
    print("2 Pick up a dog")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice=int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        dropOff()

    elif choice == 2:
        pickUp()

    elif choice == 3:
        calcCost()

    elif choice == 4:
        printRoll()

    elif choice >= 5:
        exit = input("Do you want to exit this programme? (Y/N)").upper()
        if exit == "Y":
            print()
            print("====================================================")
            print("Exiting this program.")
            print("====================================================")
            quit()
        else:
            choice = 0


def main():
    num_attending_fun_inthe_sun =0
    num_attending_active_kids = 0
    total_age_funsun = 0
    total_age_active = 0
    choices = 0

    while choices != 3:
        print("Choose one from the options:")
        print()
        print("1. Enter attendance")
        print("2. Display statistics")
        print("3. Exit")
        print()
        print("======================================================================")
        try: choice = check_number("Enter your choice "
                                   "Between number 1~3")
            if choice == 1:
                data = enter_attendance()

                if data[0] == "Fun":
                    total_age_funsun += int(data[1])
                    num_attending_fun_inthe_sun += 1

                elif data[0] == "Active"
                    total_age_active += int(data[1])
                    num_attending_active_kids += 1

            elif choice == 2:
                statistics(num_attending_fun_inthe_sun, num_attending_active_kids, total_age_active,total_age_funsun)

            elif choice == 3:
                confirm_exit = input("Do you really want to exit? Enter 'Y' to confirm, Enter 'N' to go back to main.").upper()

                if confirm_exit == "Y":
                    print()
                    print("==============================================================")
                    statistics(num_attending_fun_inthe_sun, num_attending_active_kids, total_age_active, total_age_funsun)
                    print("Exiting the program.")
                    print("==============================================================")
                    exit()
                else:
                    choice = 0
            else :
                print("Must be an integer between 1 and 3")
        except ValueError:
            print("Not a valid number")


def check_number(text):
    valid = False
    while not valid:
        try:
            number = int(input(text))
            if isinstance(number, int):
                valid = True
                return number
        except ValueError:
            print("Wrong number.")


def enter_attendance():
    group = input("Which group is the child attending? \nF = Fun in the  sun \nA Active kids")

    if group == "F":
        asking_age = int(input("How old is your child? \nThe age must be between 5 to 15."))

        while asking_age < 5 and asking_age > 15:
            











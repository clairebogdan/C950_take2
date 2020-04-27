# Claire Bogdan ID:#001210883
# Western Governors University
# Data Structures and Algorithms II (C950)


# Displays the menu again or allows the user to exit
from chaining_hashtable import auto_increment_package_id, print_search_result


def menu():
    response = input("Main Menu? \n"
                     "Enter anything to go to Main Menu \n"
                     "ENTER 0 TO EXIT \n")
    if response != "0":
        ui()
    else:
        SystemExit


# User interface where the user can view information
# about the program. It uses the menu() function in order to
# go back to the main menu to see more information
def ui():
    # Main Menu Options
    choice = input("What would you like to do? \n"
                   "[1] Package Status\n"
                   "[2] Lookup Package \n"
                   "[3] Insert New Package \n"
                   "[4] See Best Route and Mileage \n"
                   "ENTER 0 TO EXIT \n")

    try:  # tries to convert the user input to an integer
        value = int(choice)  # if this fails, it will be caught in the except

        # Main Menu Options and related actions

        # Exit the program
        if value == 0:
            print("Goodbye!")
            SystemExit

        # Package Status
        if value == 1:
            val = input("Please pick a timeslot: \n"
                        "[1] 8:35 - 9:25 \n"
                        "[2] 9:35 - 10:25 \n"
                        "[3] 12:03 - 13:12 \n")
            try:
                val = int(val)  # if this fails, it will be caught in the except
                if val == 1:
                    print("not available yet")
                if val == 2:
                    print("not available yet")
                if val == 3:
                    print("not available yet")
            except ValueError:
                print("Please only enter an integer 1-3 for the timeslot menu")
            menu()

        # Lookup Package
        if value == 2:
            # Prompt the user to get package ID to search for.
            user_search_string = input("Enter the ID of the package you would like to search for: ")
            try:
                user_search_int = int(user_search_string)
                print_search_result(user_search_int)
            except ValueError:
                print("You did not enter an integer for the ID")
            menu()

        # Insert New Package
        # Any new packages that are inserted here are only available during runtime.
        # Permanent new packages must be inserted manually into the csv file. This is to show that insertion
        # of packages would be possible through this UI, but the addition of a
        # new address could drastically change the output of this assignment.
        if value == 3:
            print("New Package: \n")

            # This data cannot be changed by the user. Prevents them from entering an invalid ID or state
            print("Auto-generated Package ID: ", auto_increment_package_id())
            print("State: UT")
            auto_new_id = auto_increment_package_id()
            state = "UT"

            # This data is available for the user to create
            new_street = input("Street Address: ")
            new_city = input("City: ")
            new_zip = input("Zip Code: ")
            new_deadline = input("Deadline for Delivery (24hr time hh:mm): ")
            new_weight = input("Weight (kg): ")

            # Special notes are not allowed to be added by the user
            no_special1 = "nan"
            no_special2 = "nan"
            no_special3 = "nan"
            no_special4 = "nan"
            new_status = "AT_HUB"

            menu()

        # See Best Route and Mileage
        if value == 4:
            print("not available yet")
            menu()


        # INVALID MENU OPTION (INT TOO BIG OR NEGATIVE)
        if value > 4 or value < 0:
            print("Please only enter an integer between 0-4")
            menu()

    except ValueError:  # the user entered a value that was NOT 0 - 4
        try_again = input("Please only enter an integer between 0-4 \n"
                          "Would you like to try again?\n"
                          "Enter anything to continue \n"
                          "ENTER 0 TO EXIT \n")
        if try_again != "0":
            ui()
        else:
            SystemExit


# Call to the user interface
print("Welcome to WGUPS! The Truck Delivery Simulation has started.")
#Call to start everything would be here
ui()

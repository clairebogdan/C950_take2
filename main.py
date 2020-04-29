# Claire Bogdan ID:#001210883
# Western Governors University
# Data Structures and Algorithms II (C950)


# Displays the menu again or allows the user to exit
from algorithm import greedy_path_algorithm
from chaining_hashtable import auto_increment_package_id, print_search_result
from truck import load_trucks_and_get_best_route, truck2, see_package_status, total_miles_traveled_by_all_trucks, \
    deliver_packages


def menu():
    response = input("Main Menu? \n"
                     "Enter anything to go to Main Menu \n"
                     "ENTER 0 TO EXIT \n")
    if response != "0":
        ui()
    else:
        SystemExit


# User interface where the user can view information about the program. It follows a strict order in order to keep
# the truck data organized
def ui():
    # Main Menu Options
    main_menu = input("What would you like to do? \n"
                   "[1] Load Trucks (Insert Packages) \n"
                   "[2] Lookup Individual Package \n"
                   "ENTER 0 TO EXIT \n")

    # [0] Exit the program
    if main_menu == "0":
        print("You entered 0 or did not enter a valid menu option.")
        print("Goodbye!")
        SystemExit

    # [1] Load Trucks
    if main_menu == "1":
        print("The time is now 8:00")
        print("Packages were inserted into hash table and packages were loaded onto trucks.")
        load_trucks_and_get_best_route()
        status_1 = input("\nEnter 1 to go package status #1 \n"
                           "[1] See package status of all packages between 8:35 a.m. and 9:25 a.m \n"
                           "ENTER 0 TO EXIT \n")

        # [0] Exit the program
        if status_1 == "0":
            print("You entered 0 or did not enter a valid menu option.")
            SystemExit

        # [1] Package status #1
        if status_1 == "1":

            see_package_status(9, 25, 0)

            # Next: Fix the package #9 address
            print("\nURGENT! IT IS 10:20AM. YOU NEED TO FIX THE ADDRESS FOR PACKAGE #9")
            fix_pkg = input("Fix address package #9? Enter 1 for YES or 0 TO EXIT: ")

            # [0] Exit the program
            if fix_pkg == "0":
                print("You entered 0 or did not enter a valid menu option.")
                SystemExit

            # [1] YES, fix the package
            if fix_pkg == "1":
                print("Fixing package #9 address to 410 S State St., Salt Lake City, UT 84111 ... ")
                print("doesnt work yet")
                '''
                print(truck2.route)
                for package in truck2.truck_packages:

                    if package[7] == "W":
                        truck2.remove(package)
                updated_package_9 = ['9', '410 S State St', 'Salt Lake City', 'UT', '84111', '17:00', '2', 'W']
                truck2.insert(updated_package_9)
                greedy_path_algorithm(truck2.route)
                print("You fixed the address!")
                print(truck2.route)
                '''

                # Next: See package status 2
                status_2 = input("\nNow, you can view package status #2\n"
                                 "[1] See package status of all packages between 9:35 a.m. and 10:25 a.m \n"
                                 "ENTER 0 TO EXIT\n")

                # [0] Exit the program
                if status_2 == "0":
                    print("You entered 0 or did not enter a valid menu option.")
                    SystemExit

                if status_2 == "1":

                    see_package_status(10, 25, 0)

                    # Next: See package status 3
                    status_3 = input("\nNow, you can view package status #3\n"
                                     "[1] See package status of all packages between 12:03 p.m. and 1:12 p.m (13:12) \n"
                                     "ENTER 0 TO EXIT\n")

                    # [0] Exit the program
                    if status_3 == "0":
                        print("You entered 0 or did not enter a valid menu option.")
                        SystemExit

                    # [1] See package status 3
                    if status_3 == "1":

                        see_package_status(13, 12, 0)

                        # Last, the user can view the final results
                        final = input("\nSee results of the truck delivery?\n"
                                      "[1] YES, see total mileage of all trucks and all package status\n"
                                      "ENTER 0 TO EXIT\n")

                        # [0] Exit the program
                        if final == "0" or final != "1":
                            print("You entered 0 or did not enter a valid menu option.")
                            SystemExit

                        # [1] See final results and exit the program!
                        if final == "1":

                            total_miles_traveled_by_all_trucks()
                            deliver_packages()
                            SystemExit

    # Lookup Individual Package
    if main_menu == "2":
        print("Reminder: The time is 7:59AM. All packages are either AT_HUB or DELAYED_ON_FLIGHT")

        checker = "1"
        while checker == "1":
            # Prompt the user to get package ID to search for.
            user_search_string = input("Enter the ID of the package you would like to search for: ")
            try:
                user_search_int = int(user_search_string)
                print_search_result(user_search_int)
            except ValueError:
                print("You did not enter an integer for the ID")
            try_again = input("Enter 1 to search again. Enter anything else to exit: ")
            checker = try_again
        ui()


print("Welcome to WGUPS! The time is 7:59AM")
ui()
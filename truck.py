# Claire Bogdan ID:#001210883
from WGUPS_graph import graph
from algorithm import greedy_path_algorithm
from chaining_hashtable import package_hashtable
from datetime import timedelta, datetime


# The Truck Class assists in creating truck objects which will be loaded with packages
class Truck:

    # Constructor to initialize packages on the truck, route, delivery start time, and mileage
    def __init__(self):
        self.truck_packages = []
        self.route = []
        self.start_time = None
        self.current_time = None
        self.finish_time = None
        self.speed = 0.3  # 18mph is equivalent to 0.3 miles / minute

    # Put package on truck
    def insert(self, package):
        self.truck_packages.append(package)  # puts the package onto the truck
        self.route.append(package[1])  # package[1] == street address where the package is going

    # Delivered packages are removed from the truck
    def remove(self, package):
        self.truck_packages.remove(package)  # takes the package off the truck
        self.route.remove(package[1])  # removes the address from the route

    # Leave the hub and start the delivery route
    def start_delivery(self, time):
        self.start_time = time

    # This is updated as deliveries are made
    def current_time(self, time):
        self.current_time = time
        return time

    # Time that the truck finished their deliveries and is back at the hub
    # This will tell truck 3 when to leave (as there are only 2 drivers)
    def returned_to_hub(self, time):
        self.finish_time = time
        return time



# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# Create an iterable list of locations used in load_trucks_and_get_best_route()
all_addresses = []

# Put the packages in the graph's delivery_dict to associate locations with packages
graph.put_packages_in_delivery_dict(package_hashtable)


# Function to load the trucks with the "correct" packages and get the best route to take
# "Correct" packages were first sorted by hand, and I determined what the priorities would be.
# Priority 1: Packages that have to be delivered by 9:00
# Priority 2: Packages that have to be delivered by 10:30 and are delayed_on_flight or have deliver_with special notes
# Priority 3: Packages that have to be delivered by 10:30 with no special notes
# Priority 4: Packages that have to be delivered by EOD (17:00) and delayed_on_flight, truck2_only, or wrong_address
# Priority 5: Packages that are EOD with no special notes, but cannot exceed the load of the trucks (16 packages)
# After all trucks are loaded, the greedy_path_algorithm changes the route to make it more efficient
# O(N^2)
def load_trucks_and_get_best_route():

    # Populates the unvisited_addresses list with the locations from the graph.
    for location in graph.delivery_dict:
        all_addresses.append(location)

    # Priority 1 (see description above)
    for address in all_addresses:
        for package in graph.delivery_dict[address]:
            if package[5] == "9:00":
                truck1.insert(package)

    # Priority 2 (see description above)
    for address in all_addresses:
        for package in graph.delivery_dict[address]:
            if package[5] == "10:30" and package[7] != "" and package[7] != "2" and package[7] != "W" and package[7] != "9:05":
                truck1.insert(package)
            elif package [5] == "10:30" and package[7] == "9:05":
                truck2.insert(package)

    # Priority 3 (see description above)
    for address in all_addresses:
        for package in graph.delivery_dict[address]:
            if package[5] == "10:30" and package[7] == "":
                truck1.insert(package)

    # Priority 4 (see description above)
    for address in all_addresses:
        for package in graph.delivery_dict[address]:
            if package[5] == "17:00" and package[7] == "9:05":
                truck2.insert(package)
            if package[5] == "17:00" and package[7] == "W":
                truck2.insert(package)
            if package[5] == "17:00" and package[7] == "2":
                truck2.insert(package)

    # Priority 5 (see description above)
    for address in all_addresses:
        for package in graph.delivery_dict[address]:
            if package[5] == "17:00" and package[7] == "":
                if len(truck1.truck_packages) < 16:
                    truck1.insert(package)
                elif len(truck2.truck_packages) < 16:
                    truck2.insert(package)
                elif len(truck3.truck_packages) < 16:
                    truck3.insert(package)
                else:
                    print("package could not be loaded")

    # Original, inefficient route for display purposes
    truck1_original_route = truck1.route
    truck1_original_route.append("4001 South 700 East")
    truck2_original_route = truck2.route
    truck2_original_route.append("4001 South 700 East")
    truck3_original_route = truck3.route
    truck3_original_route.append("4001 South 700 East")

    # Change the route to make it more efficient
    truck1.route = greedy_path_algorithm(truck1.route)
    truck2.route = greedy_path_algorithm(truck2.route)
    truck3.route = greedy_path_algorithm(truck3.route)

    # Route the trucks back to the hub
    truck1.route.append("4001 South 700 East")
    truck2.route.append("4001 South 700 East")
    truck3.route.append("4001 South 700 East")

    # Results
    print("All truck & package data after loading: ")
    print("Truck 1 has", len(truck1.truck_packages), "packages")
    print("Truck 1 packages:", *truck1.truck_packages, sep="\n")
    print("Truck 2 has", len(truck2.truck_packages), "packages")
    print("Truck 2 packages:", *truck2.truck_packages, sep="\n")
    print("Truck 3 has", len(truck3.truck_packages), "packages")
    print("Truck 3 packages:", *truck3.truck_packages, sep="\n")


# Gets the miles traveled for an individual truck
# O(N)
def miles_traveled(truck_route):
    edge_weight_list = graph.edge_weights
    miles = 0
    for i in range(0, len(truck_route) - 1):
        miles = miles + edge_weight_list[truck_route[i], truck_route[i+1]]
    return miles


# Gets the total miles traveled by all trucks
# O(N)
def total_miles_traveled_by_all_trucks():
    t1_miles = miles_traveled(truck1.route)
    t2_miles = miles_traveled(truck2.route)
    t3_miles = miles_traveled(truck3.route)
    total = t1_miles + t2_miles + t3_miles
    print("Truck 1: ", round(t1_miles, 2), "+ Truck 2: ", round(t2_miles, 2),
          "+ Truck 3: ", round(t3_miles, 2), " TOTAL =", round(total, 2), "miles")


# Assists with stating the time of the package delivery
# O(1)
def add_seconds(time, sec):
    date = datetime(100, 1, 1, time.hour, time.minute, time.second)
    date = date + timedelta(seconds = sec)
    return date.time()


# This function delivers all the packages to the correct address
# O(N^2)
def deliver_packages():
    miles_between = graph.edge_weights

    # Truck 1 Delivery
    truck1_start = datetime(2020, 1, 1, 8, 0, 0)
    truck1.start_time = truck1_start
    truck1.current_time = truck1_start
    for i in range(0, len(truck1.route) - 1):
        distance = miles_between[truck1.route[i], truck1.route[i+1]]
        speed = truck1.speed
        minutes_decimal = distance/speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck1.current_time, seconds_to_add)
        truck1.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "DELIVERED AT", str(delivered_time)
        for package in truck1.truck_packages:
            if truck1.route[i+1] == package[1]:
                package[8] = updated_delivery_status
    truck1.finish_time = truck1.current_time
    print("Truck 1 Delivery:", *truck1.truck_packages, sep="\n")  # prints using new lines instead of a giant line

    # Truck 2 Delivery
    truck2_start = datetime(2020, 1, 1, 9, 5, 0)
    truck2.start_time = truck2_start
    truck2.current_time = truck2_start
    for i in range(0, len(truck2.route) - 1):
        distance = miles_between[truck2.route[i], truck2.route[i + 1]]
        speed = truck2.speed
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck2.current_time, seconds_to_add)
        truck2.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "DELIVERED AT", str(delivered_time)
        for package in truck2.truck_packages:
            if truck2.route[i + 1] == package[1]:
                package[8] = updated_delivery_status
    truck2.finish_time = truck2.current_time
    print("Truck 2 Delivery:", *truck2.truck_packages, sep="\n") # prints using new lines instead of a giant line

    # Truck 3 Delivery
    truck3_start = truck1.finish_time
    truck3.start_time = truck3_start
    truck3.current_time = truck3_start
    for i in range(0, len(truck3.route) - 1):
        distance = miles_between[truck3.route[i], truck3.route[i + 1]]
        speed = truck3.speed
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck3.current_time, seconds_to_add)
        truck3.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
        updated_delivery_status = "DELIVERED AT", str(delivered_time)
        for package in truck3.truck_packages:
            if truck3.route[i + 1] == package[1]:
                package[8] = updated_delivery_status
    truck3.finish_time = truck3.current_time
    print("Truck 3 Delivery:", *truck3.truck_packages, sep="\n") # prints using new lines instead of a giant line


# Changes the delivery status to "out for delivery"
# O(N)
def out_for_delivery(truck_packages):
    for package in truck_packages:
        package[8] = "OUT_FOR_DELIVERY"


# Allows the user in main.py to view packages' delivery status at certain times
# O(N^2)
def see_package_status(hour, min, sec):
    miles_between = graph.edge_weights
    stop_time = datetime(2020, 1, 1, hour, min, sec)

    # Truck 1 Delivery
    truck1_start = datetime(2020, 1, 1, 8, 0, 0)
    truck1.start_time = truck1_start
    truck1.current_time = truck1_start
    out_for_delivery(truck1.truck_packages)
    for i in range(0, len(truck1.route) - 1):
        distance = miles_between[truck1.route[i], truck1.route[i + 1]]
        speed = truck1.speed
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck1.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck1.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "DELIVERED AT", str(delivered_time)
            for package in truck1.truck_packages:
                if truck1.route[i + 1] == package[1]:
                    package[8] = updated_delivery_status
    truck1.finish_time = truck1.current_time
    print("Truck 1 Delivery:", *truck1.truck_packages, sep="\n")  # prints using new lines instead of a giant line

    # Truck 2 Delivery
    truck2_start = datetime(2020, 1, 1, 9, 5, 0)
    truck2.start_time = truck2_start
    truck2.current_time = truck2_start
    out_for_delivery(truck2.truck_packages)
    for i in range(0, len(truck2.route) - 1):
        distance = miles_between[truck2.route[i], truck2.route[i + 1]]
        speed = truck2.speed
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck2.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck2.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "DELIVERED AT", str(delivered_time)
            for package in truck2.truck_packages:
                if truck2.route[i + 1] == package[1]:
                    package[8] = updated_delivery_status
    truck2.finish_time = truck2.current_time
    print("Truck 2 Delivery:", *truck2.truck_packages, sep="\n")  # prints using new lines instead of a giant line

    # Truck 3 Delivery
    truck3_start = truck1.finish_time
    truck3.start_time = truck3_start
    truck3.current_time = truck3_start
    out_for_delivery(truck3.truck_packages)
    for i in range(0, len(truck3.route) - 1):
        distance = miles_between[truck3.route[i], truck3.route[i + 1]]
        speed = truck3.speed
        minutes_decimal = distance / speed
        seconds_to_add = round(minutes_decimal * 60, 2)
        delivered_time = add_seconds(truck3.current_time, seconds_to_add)
        if delivered_time < stop_time.time():
            truck3.current_time = datetime(2020, 1, 1, delivered_time.hour, delivered_time.minute, delivered_time.second)
            updated_delivery_status = "DELIVERED AT", str(delivered_time)
            for package in truck3.truck_packages:
                if truck3.route[i + 1] == package[1]:
                    package[8] = updated_delivery_status
    truck3.finish_time = truck3.current_time
    print("Truck 3 Delivery:", *truck3.truck_packages, sep="\n")  # prints using new lines instead of a giant line





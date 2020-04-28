# Claire Bogdan ID:#001210883
# The Truck Class assists in creating truck objects which will be loaded with packages
from WGUPS_graph import Graph, get_graph
from chaining_hashtable import package_hashtable


class Truck:

    # Constructor to initialize packages on the truck, route, delivery start time, and mileage
    def __init__(self):
        self.truck_packages = []
        self.route = []
        self.start_time = None
        self.total_miles_traveled = 0

    # Put package on truck
    def insert(self, package):
        self.truck_packages.append(package)  # puts the package onto the truck
        self.route.append(package[1])  # package[1] == street address where the package is going

    # Leave the hub and start the delivery route
    def start_delivery(self, time):
        self.start_time = time
        for package in self.truck_packages:
            package[8] = "OUT_FOR_DELIVERY"

    # Delivered packages are removed from the truck
    def remove(self, package):
        self.truck_packages.remove(package)  # takes the package off the truck
        self.route.remove(package[1])  # removes the address from the route


# Create truck objects
truck1 = Truck()
truck1.start_delivery("8:00")

truck2 = Truck()
truck2.start_delivery("9:05")

truck3 = Truck()
#truck3.start_delivery(??) When truck1 gets back

all_addresses = []
#truck1_graph = Graph()
#truck2_graph = Graph()
#truck3_graph = Graph()

# Initialize graph and put the packages in the delivery dictionary to associate locations with packages
graph = get_graph("WGUPS_distances.csv")
graph.put_packages_in_delivery_dict(package_hashtable)
# print("Entire graph delivery dictionary: ", graph.delivery_dict)


# Function to load the trucks with the "correct" packages
# "Correct" packages were first sorted by hand, and I determined what the priorities would be.
# Priority 1: Packages that have to be delivered by 9:00
# Priority 2: Packages that have to be delivered by 10:30 and are delayed_on_flight or have deliver_with special notes
# Priority 3: Packages that have to be delivered by 10:30 with no special notes
# Priority 4: Packages that have to be delivered by EOD (17:00) and delayed_on_flight, truck2_only, or wrong_address
# Priority 5: Packages that are EOD with no special notes, but cannot exceed the load of the trucks (16 packages)

# Key for package indices:
# package[0] = package_id
# package[1] = street
# package[2] = city
# package[3] = state
# package[4] = zip
# package[5] = deadline
# package[6] = weight(kg)
# package[7] = special_notes (2 = truck2_only, 9:05 = delayed_on_flight, W = wrong_address, ##/## = deliver_with)
# package[8] = delivery_status (AT_HUB, OUT_FOR_DELIVERY, or DELIVERED)


# O(N^2)
def load_trucks():

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

    # FINALLY: Route the trucks back to the hub
    truck1.route.append("4001 South 700 East")
    truck2.route.append("4001 South 700 East")
    truck3.route.append("4001 South 700 East")

    # Print statements to assist with debugging
    print("Amount on Truck 1: ", len(truck1.truck_packages))
    print("Truck 1 Packages: ", truck1.truck_packages)
    print("Truck 1 route: ", truck1.route, "\n")
    print("Amount on Truck 2: ", len(truck2.truck_packages))
    print("Truck 2 Packages: ", truck2.truck_packages)
    print("Truck 2 route: ", truck2.route, "\n")
    print("Amount on Truck 3: ", len(truck3.truck_packages))
    print("Truck 3 Packages: ", truck3.truck_packages)
    print("Truck 3 route: ", truck3.route, "\n")





load_trucks()



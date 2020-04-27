# The Truck Class assists in creating truck objects which will be loaded with packages
from WGUPS_graph import Graph, get_graph
from chaining_hashtable import package_hashtable

# graph = get_graph("WGUPS_distances.csv")

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
truck2 = Truck()
truck3 = Truck()
unvisited_addresses = []
#truck1_graph = Graph()
#truck2_graph = Graph()
#truck3_graph = Graph()



# Function to load the trucks with the "correct" packages
# "Correct" packages were first sorted by hand, and I determined what the priorities would be.
# Priority 1: Packages that have to be delivered by 9:00
# Priority 2: Packages that have to be delivered by 10:30 and are arriving late (delayed_on_flight)
# Priority 3: Packages that have to be delivered by 10:30 with no special notes
# Priority 4: Packages that have to be delivered by EOD and are truck2_only or wrong_address
# Priority 5: Packages that are EOD with no special notes, but cannot exceed the load of the trucks (16 packages)


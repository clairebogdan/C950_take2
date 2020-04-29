# Claire Bogdan ID:#001210883
from WGUPS_graph import graph


# Greedy algorithm is used to determine the best path for each truck
# Every truck will always start at the hub
# As packages are loaded to the truck (with their attached addresses), the algorithm will sort the route and determine
# the best path (the "next" location will be the one with the shorter distance from point a to point b.)
# O(N^2)
def greedy_path_algorithm(route):
    start = "4001 South 700 East"  # all trucks start their deliveries at the hub
    graph_edge_weights = graph.edge_weights  # get the edge weights from the graph
    truck_route_to_sort = route  # this is the route created initially as packages were loaded to the truck

    greedy_path = [start]  # the greedy_path will be the better route to take, starting at the hub

    # using a while loop because the truck_route_to_sort will have
    # locations removed as they are added to the greedy_path
    while len(truck_route_to_sort) != 0:
        min = [0, start]  # "0" is the edge weight and "start" is the address, which will change throughout the loop
        for location in truck_route_to_sort:
            distance = graph_edge_weights[greedy_path[-1], location]  # get the edge weights between each location
            if min[0] == 0:  # helps establish starting location as well as self-loops to the same location
                min = [distance, location]
            if distance < min[0] and distance != 0:
                min = [distance, location]
        if min[1] not in greedy_path:  # eliminates double visits to the same place
            greedy_path.append(min[1])
        truck_route_to_sort.remove(min[1])  # removes the location and repeat the while loop until empty

    # This is the better route for the truck to take
    return greedy_path

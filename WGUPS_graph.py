# Claire Bogdan ID:#001210883
# This file takes data from the distance csv file, creates vertices based on the name of the location,
# and graphs the data using undirected edges. Each edge has a weight that represents the miles between each vertex
import csv


class Graph:

    # Constructor creating empty lists for the locations and edge weights
    def __init__(self):
        self.delivery_dict = {}  # has the same function of an adjacency list
        self.edge_weights = {}

    # Adds a vertex to the graph
    def add_vertex(self, vertex):
        self.delivery_dict[vertex] = []  # creates a dictionary with the street address as the key

    # Adds an undirected edge between vertices. Weight is equivalent to miles
    def add_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weights[(vertex_a, vertex_b)] = weight  # creates a dict where key : value == vertices : miles

    # Associates each package with its corresponding vertex on the graph
    # O(N^2)
    def put_packages_in_delivery_dict(self, ht):
        for bucket in ht.table:
            for item in bucket:
                self.delivery_dict[item[1]].append(item)


# This function grabs the entire distance csv file.
# This is needed in order to create edges between vertex_a and vertex_b
# O(N)
def get_all_distance_csv_data(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data


# This function creates the graph
# O(N)
def get_graph(filename):
    data = get_all_distance_csv_data(filename)
    graph_distances = Graph()
    for row in data:
        graph_distances.add_vertex(row[1])  # Vertex is associated with the street address
    for row in data:
        for i in range(3, len(row)):  # Starts at 3 because indices 0-2 are name, street, and zip, which are not needed
            graph_distances.add_edge(row[1], data[i-3][1], float(row[i]))  # data[i-3][1] gets each connected street vertex
    return graph_distances


# Initialize the graph for further use
graph = get_graph("WGUPS_distances.csv")


# Prints useful information
# print(graph.delivery_dict)
print(graph.edge_weights['4001 South 700 East', '4001 South 700 East'])



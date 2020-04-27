# The Chaining Hash Table improves the speed at which packages can be accessed

import csv


class ChainingHashTable:

    # Constructor with 10 buckets, initialized to empty
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert a new package into the hashtable, using the first index of the data extracted from the csv as the key,
    # since the first index is the package ID
    def insert(self, key, package):
        package[0] = int(package[0])
        bucket = key % len(self.table)
        self.table[bucket].append(package)
        package.append("AT_HUB")

    # Search for a package with matching input key (matching package ID)
    def search(self, key):

        # Get the bucket list where this key/ID should be found
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        # Inside the bucket, search for the corresponding package ID
        for package in bucket_list:
            if package[0] == key:
                return package  # Package was found, returns package information
        return None  # Package was not found

    # Remove a package with matching input key (matching package ID)
    def remove(self, key):

        # Get the bucket list where this key/ID should be found
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Look inside the bucket and remove package for the matching key/ID, if found.
        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove(key)



# Extracts data from the csv file that contains packages
# Enters the package data into the hashtable
# O(N)
def get_packages(filename):
    hash_pkgs = ChainingHashTable()
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # skips the header
        for row in csv_reader:
            hash_pkgs.insert(int(row[0]), row)  # row[0] is the package ID, row is all package information
    return hash_pkgs


# Initialize the package hashtable
package_hashtable = get_packages("WGUPS_packages.csv")


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


# See package data in the hashtable
# print(package_hashtable.table)

def auto_increment_package_id():
    package_ids = []
    with open("WGUPS_packages.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # skips the header
        for row in csv_reader:
            package_ids.append(int(row[0]))
    return max(package_ids) + 1


def print_search_result(id):
    result = package_hashtable.search(id)
    print(result)
print("NEVAN KUMAR")
print("22053791")
# Function to take user input and create a set
def input_set():
    elements = input("Enter elements of the set (comma separated): ").split(',')
    return set(map(int, elements))  # Convert input strings to integers and return as a set

# Input for two sets
set1 = input_set()
set2 = input_set()

# Union of sets (all unique elements from both sets)
union_set = set1 | set2  # or set1.union(set2)
print("Union:", union_set)

# Intersection of sets (common elements between both sets)
intersection_set = set1 & set2  # or set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference of sets (elements in set1 but not in set2)
difference_set = set1 - set2  # or set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference (elements in either set1 or set2, but not both)
symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)
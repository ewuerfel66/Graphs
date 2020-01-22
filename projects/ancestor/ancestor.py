import 

class FamilyTree:
    def __init__(self):
        self.members = {}

    def add_parent_child(self, parent_child_tuple):
        # Get parent and child id
        parent, child = parent_child_tuple[0], parent_child_tuple[1]

        # If one or both aren't in the FamilyTree, add them
        if parent not in self.members:
            self.members[parent] = set()

        if child not in self.members:
            self.members[child] = set()

        # Add relationship pointing child --> parent
        self.members[child].add(parent)

    def get_parents(self, starting_node):
        return self.members[starting_node]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    # Instantiate family & possible paths list
    family = FamilyTree()
    possible_paths = []

    # Add members
    for pair in test_ancestors:
        family.add_parent_child(pair)

    # If starting_node has no parents, return -1
    if family.get_parents(starting_node) == set():
        return -1

    # Find all possible paths
    # First, start possible_paths out with lists containing starting_node's parents
    for parent in family.get_parents(starting_node):
        possible_paths.append([parent])

    # # Loop through possible paths and update if they have parents
    # for path in possible_paths:
    #     if family.get_parents(path[-1]) != set():
    #         # Create a new path for each parent
    #         for parent in family.get_parents(path[-1]):
    #             new_path = path.append(parent)
    #             possible_paths.append(new_path)
    #         # Get rid of old path
    #         # possible_paths.remove(path)

    #     else:
    #         pass

    for path in possible_paths:
        for parent in family.get_parents(path[-1]):
            print(parent)


    return possible_paths

    # while family.get_parents(starting_node) != set():
    #     for parent in family.get_parents(starting_node):


    # Return the last member in the longest path



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# family = FamilyTree()

# for pair in test_ancestors:
#     family.add_parent_child(pair)

# for parent in family.get_parents(6):
#     print(parent)

print(earliest_ancestor(test_ancestors, 3))
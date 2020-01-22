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
    # Instantiate family & longest path & stack & visited
    family = FamilyTree()
    longest_path = []
    stack = Stack()
    visited = set()

    # Add members
    for pair in ancestors:
        family.add_parent_child(pair)

    # If starting_node has no parents, return -1
    if family.get_parents(starting_node) == set():
        return -1

    # Add starting node to stack
    stack.push([starting_node])

    # While stack is not empty:
    while stack.size() > 0:

        # Pop the path and get the last node
        path = stack.pop()
        node = path[-1]

        # If the node hasn't been visited:
        if node not in visited:

            # Mark as visited
            visited.add(node)

            # Add all it's neighbors
            for parent in family.get_parents(node):

                # Copy & append to path
                new_path = path.copy()
                new_path.append(parent)

                # See if it's our longest_path
                if len(new_path) > len(longest_path):
                    longest_path = new_path

                # push back to stack
                stack.push(new_path)

    # Return the last ancestor in the longest_path
    return longest_path[-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# family = FamilyTree()

# for pair in test_ancestors:
#     family.add_parent_child(pair)

# for parent in family.get_parents(6):
#     print(parent)

print(earliest_ancestor(test_ancestors, 8))
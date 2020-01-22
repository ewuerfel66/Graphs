"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue and enqueue starting vertex_id
        queue = Queue()
        queue.enqueue(starting_vertex)

        # Create an empty set to store visited vertices
        visited = set()

        # While Queue is not empty:
        while queue.size() > 0:
            
            # Dequeue the first vertex
            vertex = queue.dequeue()

            # If that vertex hasn't been visited:
            if vertex not in visited:

                # Mark as visited
                print(vertex)
                visited.add(vertex)

                # Add all it's neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack and push starting vertex_id
        stack = Stack()
        stack.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While stack is not empty:
        while stack.size() > 0:

            # Pop the vertex
            vertex = stack.pop()

            # If that vertex hasn't been visited:
            if vertex not in visited:

                # Mark as visited
                print(vertex)
                visited.add(vertex)

                # Add all it's neighbors
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # python instantiates at compiling, this handles repeat use
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                print(child_vertex)
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Stack and push starting vertex_id
        queue = Queue()
        queue.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While stack is not empty:
        while queue.size() > 0:

            # Pop the vertex
            path = queue.dequeue()
            vertex = path[-1]

            # If that vertex hasn't been visited:
            if vertex not in visited:

                # Return the path
                if vertex == destination_vertex:
                    return path
                
                # Mark as visited
                visited.add(vertex)

                # Add all it's neighbors
                for neighbor in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack and push starting vertex_id
        stack = Stack()
        stack.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While stack is not empty:
        while stack.size() > 0:

            # Pop the vertex
            path = stack.pop()
            vertex = path[-1]

            # If that vertex hasn't been visited:
            if vertex not in visited:

                # Return the path
                if vertex == destination_vertex:
                    return path
                
                # Mark as visited
                visited.add(vertex)

                # Add all it's neighbors
                for neighbor in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print("")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("")
    graph.dft_recursive(1)
    print("")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))

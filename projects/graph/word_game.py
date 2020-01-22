# Import graph
from graph import Graph
import time


# Import words from words.txt
with open("words.txt") as f:
    words = f.readlines()

words = [word.strip().lower() for word in words]


# Helper function to see if word is one letter off
def one_letter_off(w1, w2):
    diff_count = 0
    word_length = len(w1)

    for i in range(word_length):
        if w1[i] != w2[i]:
            diff_count += 1
        else:
            pass

    if diff_count == 1:
        return True
    else:
        return False

# Helper function to pull all words of same length
def same_length(words, length):
    return [word for word in words if len(word) == length]

def shortest_path(w1, w2):
    # If w1 and w2 aren't the same len, return None
    if len(w1) != len(w2):
        return None

    # Take all words of the same length
    eligible_words = same_length(words, len(w1))

    # Enter eligible words into graph
    # Instantiate Graph
    graph = Graph()

    # Add each eligible word as a vertex in the graph
    for word in eligible_words:
        graph.add_vertex(word)

    # For each vertex, iterate through other vertices
    for vertex1 in graph.vertices:
        for vertex2 in graph.vertices:
            # If one_letter_off, add an edge
            if one_letter_off(vertex1, vertex2):
                graph.add_edge(vertex1, vertex2)

    # Do a Breadth-First Search
    return graph.bfs(w1, w2)

start_time = time.time()

print(shortest_path("sail", "boat"))

end_time = time.time()

print(end_time - start_time)
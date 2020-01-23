import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            name = "user_" + str(self.last_id + 1)
            self.add_user(name)

        # Create friendships
        for user in self.users:
            # Create a list of all possible friendships
            other_users = [other_user for other_user in self.users]
            other_users.remove(user)

            # Remove existing friendships
            for friend in self.friendships[user]:
                if friend in other_users:
                    other_users.remove(friend)

            potential_friendships = [(user, other_user) for other_user in other_users]

            # Shuffle
            random.shuffle(potential_friendships)

            # Grab the first N
            friendships = potential_friendships[:avg_friendships]

            # Add the friends
            for friendship in friendships:
                self.add_friendship(friendship[0], friendship[1])


    # def populate_graph(self, num_users, avg_friendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments

    #     Creates that number of users and a randomly distributed friendships
    #     between those users.

    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph
    #     self.last_id = 0
    #     self.users = {}
    #     self.friendships = {}
    #     # !!!! IMPLEMENT ME

    #     # Add users
    #     for i in range(num_users):
    #         name = "user_" + str(self.last_id + 1)
    #         self.add_user(name)

    #     # Create friendships
    #     for user in self.users:
    #         # Create a list of all possible friendships
    #         other_users = [other_user for other_user in self.users]
    #         other_users.remove(user)

    #         # Remove existing friendships
    #         for friend in self.friendships[user]:
    #             if friend in other_users:
    #                 other_users.remove(friend)

    #         potential_friendships = [(user, other_user) for other_user in other_users]

    #         # Shuffle
    #         random.shuffle(potential_friendships)

    #         # Grab the first N
    #         friendships = potential_friendships[:avg_friendships]
    #         # j = 0
    #         # friendships = []

    #         # while len(self.friendships[user]) < avg_friendships:
    #         #     try:
    #         #         self.add_friendship(potential_friendships[j][0], potential_friendships[j][1])
    #         #         j += 1
    #         #     except IndexError:
    #         #         pass

    #         # Add the friends
    #         for friendship in friendships:
    #             self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()

        # add starting node to queue
        queue.enqueue([user_id])

        # While the queue is not empty:
        while queue.size() > 0:
            # Pop the path
            path = queue.dequeue()
            node = path[-1]

            # If not visited:
            if node not in visited:
                # add the last entry as key, and path as value
                visited[node] = path

                # Add all it's neighbors:
                for friend in self.friendships[node]:
                    # Copy path to avoid error
                    new_path = list(path)
                    new_path.append(friend)
                    queue.enqueue(new_path)

        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

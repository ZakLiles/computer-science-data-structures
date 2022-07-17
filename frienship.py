"""Example of an undirected graph."""

from queue import Queue


class Node():
    """Node in a graph representing a person."""

    def __init__(self, name, adjacent=None):
        """Create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        assert isinstance(adjacent, set), \
            "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """Debugging-friendly representation"""

        return f"<Node: {self.name}>"


class FriendGraph():
    """Graph holding people and their friendships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return f"<FriendGraph: { {n.name for n in self.nodes} }>"

    def add_person(self, person):
        """Add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """Set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def add_people(self, people_list):
        """Add a list of people to our graph"""

        for person in people_list:
            self.add_person(person)

    def are_connected(self, person1, person2):
        """Are two people connected? Breadth-first search."""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

    def print_friends(self):

        for friend in self.nodes:
            print(friend.name)


def make_simple_friendship(friends_list):

    person1 = Node(friends_list[0])
    person2 = Node(friends_list[1])
    person3 = Node(friends_list[2])

    friends = FriendGraph()
    friends.add_people([person1, person2, person3])

    friends.set_friends(person1, person2)
    friends.set_friends(person1, person3)
    friends.set_friends(person2, person3)

    return friends


if __name__ == "__main__":
    friends_list = ["Harry", "Ron", "Hermione"]
    friends = make_simple_friendship(friends_list)
    friends.print_friends()
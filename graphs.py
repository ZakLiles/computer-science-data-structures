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

    def are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                if self.are_connected_recursive(person, person2, seen):
                    return True

        return False

    def verbose_are_connected_recursive(self, person1, person2, seen=None):
        """Are two people friends? Recursive depth-first search."""

        if not seen:
            seen = set()

        if person1 is person2:
            print(f"\nreturning True - {person1.name} is {person2.name}")
            return True

        seen.add(person1)  # Keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                print(f"calling method on {person1.name}'s friend {person.name} with {person2.name}")
                if self.verbose_are_connected_recursive(person, person2, seen):
                    print(f"\nreturning True from checking {person.name}")
                    return True

        print(f"returning False from checking {person1.name}")
        return False


# Add sample friends
harry = Node("Harry")
hermione = Node("Hermione")
ron = Node("Ron")
neville = Node("Neville")
trevor = Node("Trevor")
fred = Node("Fred")
draco = Node("Draco")
crabbe = Node("Crabbe")
goyle = Node("Goyle")

friends = FriendGraph()
friends.add_people([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

friends.set_friends(harry, hermione)
friends.set_friends(harry, ron)
friends.set_friends(harry, neville)
friends.set_friends(hermione, ron)
friends.set_friends(neville, hermione)
friends.set_friends(neville, trevor)
friends.set_friends(ron, fred)
friends.set_friends(draco, crabbe)
friends.set_friends(draco, goyle)

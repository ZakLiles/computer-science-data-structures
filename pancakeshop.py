class Stack():
    """LIFO stack.

    Implemented using a Python list; since stacks just need
    to pop and push, a list is a good implementation, as
    these are O(1) for native Python lists. However, in cases
    where performance really matters, it might be best to
    use a Python list directly, as it avoids the overhead
    of a custom class.

    Or, for even better performance (& typically smaller
    memory footprint), you can use the `collections.deque`
    object, which can act like a stack.

    (We could also write our own LinkedList class for a
    stack, where we push things onto the head and pop things
    off the head (effectively reversing it), but that would be less
    efficient than using a built-in Python list or a
    `collections.deque` object)
    """

    def __init__(self, inlist=None):
        if inlist:
            self._list = inlist
        else:
            self._list = []

    def __repr__(self):
        if not self._list:
            return "<Stack (empty)>"
        else:
            return f"<Stack tail={self._list[-1]} length={len(self._list)}>"

    def __iter__(self):
        """Allow iteration over list.

        __iter__ is a special method that, when defined,
        allows you to loop over a list, so you can say things
        like "for item in my_stack", and it will pop
        successive items off.
        """

        while True:
            try:
                yield self.pop()
            except StackEmptyError:
                raise StopIteration

    def push(self, item):
        """Add item to end of stack."""

        self._list.append(item)

    def pop(self):
        """Remove item from end of stack and return it."""

        if not self._list:
            raise StackEmptyError()

        return self._list.pop()


    def length(self):
        """Return length of stack."""

        return len(self._list)

    def peek(self):
        """Return, but don't remove, top item."""

        if self.is_empty():
            return None

        return self._list[-1]

    def empty(self):
        """Empty stack."""

        self._list = []

    def is_empty(self):
        """Is stack empty?"""

        return not bool(self._list)

    def double_pop(self):

        item1 = self._list.pop()
        item2 = self._list.pop()

        return item2, item1


def make_short_stack(list):
    short_stack = Stack()

    for item in list:
        short_stack.push(item)

    return short_stack


if __name__ == '__main__':
    list = ["yamaha", "kawasaki", "triumph", "honda", "ktm"]

    short_stack = make_short_stack(list)

    print(short_stack)

    print(short_stack.double_pop())

    print(short_stack)

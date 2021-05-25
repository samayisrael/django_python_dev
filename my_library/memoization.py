class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError(
                'Index was negative. '
                'No such thing as a negative index in a series.'
            )

        # Base cases
        if n in [0, 1]:
            return n

        # See if we've already calculated this
        if n in self.memo:
            print "grabbing memo[%i]" % n
            return self.memo[n]

        print "computing fib(%i)" % n
        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result



class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):

    def __init__(self):
        self.max_element = 0

    def get_max(self):
        self.max_element =


myStack = Stack()
myStack.push()
print(has_cycle)

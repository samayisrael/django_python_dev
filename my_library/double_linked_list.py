class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node(data)

            current = self.head
            while current.next:
                current = current.next

            new_node.prev = current
            new_node.next = None
            current.next = new_node

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def reverse(self):
        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        dup_values = {}
        current = self.head

        while current:
            if current.data not in dup_values:
                dup_values[current.data] = 1
                current = current.next
            else:
                next = current.next
                self.delete_node(current)
                current = next

    def delete_node(self, node):
        current = self.head
        while current:
            if current == node and current == self.head:
                # Case 1 - We are deleting the head Node and its the only Node
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                # Case 2 - We are deleting the head Node and it's not the only Node
                    next = current.next
                    current.next = None
                    current = None
                    next.prev = None
                    self.head = next
                    return
            elif current == node:
                if current.next:
                # Case 3 In the middle somewhere
                    prev = current.prev
                    next = current.next
                    prev.next = next
                    next.prev = prev
                    current.prev = None
                    current.next = None
                    current = None
                    return
                else:
                # Case 4 It's the last Node
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next


    def delete(self, key):
        current = self.head
        while current:
            if current.data == key and current == self.head:
                # Case 1 - We are deleting the head Node and its the only Node
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                # Case 2 - We are deleting the head Node and it's not the only Node
                    next = current.next
                    current.next = None
                    current = None
                    next.prev = None
                    self.head = next
                    return
            elif current.data == key:
                if current.next:
                # Case 3 In the middle somewhere
                    prev = current.prev
                    next = current.next
                    prev.next = next
                    next.prev = prev
                    current.prev = None
                    current.next = None
                    current = None
                    return
                else:
                # Case 4 It's the last Node
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def pairs_with_sum(self, n):
        pairs = []
        current = self.head
        while current and current.next:
            rest = current.next
            while rest:
                if current.data + rest.data == n:
                    pairs.append('(' + str(current.data) + ',' + str(rest.data) + ')')
                rest = rest.next
            current = current.next
        return pairs

    def add_after_node(self, key, data):
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.append(data)
                return
            elif current.data == key:
                new_node = Node(data)
                next = current.next
                current.next = new_node
                new_node.next = next
                new_node.prev = current
                next.prev = new_node
            current = current.next



    def add_before_node(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
                return
            current = current.next


    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)

dlist.add_before_node(1,11)
dlist.add_before_node(2,12)
dlist.add_before_node(5,15)

#print(dlist.pairs_with_sum(5))
#dlist.remove_duplicates()
#dlist.reverse()
#dlist.delete(1)
dlist.print_list()

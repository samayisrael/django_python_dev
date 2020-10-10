class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('prev_node does not exist')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        # the node to delete is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None

        # the node to delete is not the head
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print('Node to delete not found.')
            return

        prev.next = current.next
        current = None

    def delete_node_at_pos(self, pos):
        current = self.head

        if pos == 0:
            self.head = current.next
            current = None
            return

        counter = 0
        prev = None

        while current and counter != pos:
            prev = current
            current = current.next
            counter +=1

        if current is None:
            print('Node to delete not found.')
            return

        prev.next = current.next
        current = None

    def len_iterative(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.len_recursive(node.next)

    def count_occurences_iterative(self, data):
        count = 0
        current = self.head

        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def count_occurences_recursive(self, node, data):
        if node is None:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def remove_duplicates(self):
        dup_values = {}
        current = self.head
        prev = current

        while current:
            if current.data in dup_values:
                prev.next = current.next
                current = None
            else:
                dup_values[current.data] = 1
                prev = current
            current = prev.next


    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        curr_1 = self.head
        prev_1 = None
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        curr_2 = self.head
        prev_2 = None
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        # two conditions to Match
        # one of the swap nodes is the head node
        # neither of the swap nodes is the head node

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # swap the nexts
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def move_tail_to_head(self):
        last = self.head
        second_to_last = None

        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

    def rotate(self, k):
        p = self.head
        q = self.head

        prev = None
        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count +=1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        # last element to point to head
        q.next = self.head
        self.head = p.next
        p.next = None

    def sum_two_lists(self, llist):
        llist_1 = self.head
        llist_2 = llist.head
        sum_llist = LinkedList()
        carry = 0

        while llist_1 or llist_2:
            # account for different list lengths
            if not llist_1:
                i = 0
            else:
                i = llist_1.data

            if not llist_2:
                j = 0
            else:
                j = llist_2.data

            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            # move pointers
            if llist_1:
                llist_1 = llist_1.next
            if llist_2:
                llist_2 = llist_2.next
        sum_llist.print_list()




    def merge_two_sorted_lists(self, llist):

        llist_1 = self.head
        llist_2 = llist.head
        s = None


        if not llist_1:
            return llist_2
        if not llist_2:
            return llist_1

        if llist_1 and llist_2:
            if llist_1.data <= llist_2.data:
                s = llist_1
                llist_1 = llist_1.next
            else:
                s = llist_2
                llist_2 = llist_2.next

        new_head = s

        while llist_1 and llist_2:
            if llist_1.data <= llist_2.data:
                s.next = llist_1
                s = llist_1
                llist_1 = s.next
            else:
                s.next = llist_2
                s = llist_2
                llist_2 = s.next

        if not llist_1:
            s.next = llist_2
        if not llist_2:
            s.next = llist_1

        return new_head

    def is_palindrome(self):
        # String Method
        '''
        s = ''
        p = self.head

        while p:
            s += p.data
            p = p.next
        return s == s[::-1]
        '''
        # Stack Method
        s = []
        p = self.head

        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def print_nth_from_last(self, n):

        current = self.head
        total_length = self.len_iterative()

        while current:
            if total_length == n:
                print(current.data)
            total_length -=1
            current = current.next
        if current is None:
            return


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')

llist.print_nth_from_last(3)
#print(llist.is_palindrome())
#llist.merge_two_sorted_lists(llist2)
#llist.sum_two_lists(llist2)
#llist.print_list()
#llist.rotate(4)
#llist.move_tail_to_head()
#llist.swap_nodes('A','C')
#llist.remove_duplicates()
#print(llist.count_occurences_recursive(llist.head,'1'))
#print(llist.len_recursive(llist.head))
#llist.insert_after_node(llist.head.next,'E')
#llist.delete_node_at_pos(4)
#llist.print_list()

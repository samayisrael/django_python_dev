class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root)
        elif traversal_type == 'reverse_levelorder':
            return self.reverse_levelorder_print(self.root)
        else:
            print('Traversal Type ' + str(traversal_type) + ' is not supported.')
            return False

    def preorder_print(self, start, traversal):
        #  Root -> Left -> Right
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        #  left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        #  left -> Right -> Root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        from collections import deque
        queue = deque()
        queue.appendleft(start)
        traversal = ''

        while len(queue) > 0:
            traversal += str(queue[-1].value) + '-'
            node = queue.pop()

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        from collections import deque
        queue = deque()
        stack = deque()
        queue.appendleft(start)

        traversal = ''

        while len(queue) > 0:
            node = queue.pop()
            stack.append(node)

            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)

        while stack:
            node = stack.pop()
            traversal += str(node.value) + '-'

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left)+self.size_(node.right)

    def size(self):
        if self.root is None:
            return 0

        from collections import deque
        stack = deque()
        stack.append(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)

        return size
'''
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size_(tree.root))



print(tree.print_tree('postorder'))
nodes = list(tree.print_tree('inorder').split('-'))
print(nodes)
'''
#print(list(nodes.split('-')))
#len(nodes)-1
#print(tree.height(tree.root))
#print(tree.print_tree('reverse_levelorder'))

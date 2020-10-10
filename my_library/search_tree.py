class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)
        else:
            print('Value is already in tree')

    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, value, current):
        if value > current.value and current.right:
            return self._find(value, current.right)
        elif value < current.value and current.left:
            return self._find(value, current.left)
        if value == current.value:
            return True

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

    def inorder_print_tree(self):
        #  left -> Root -> Right
        if self.root:
            self._inorder_print_tree(self.root)


    def _inorder_print_tree(self, current):
        if current:
            self._inorder_print_tree(current.left)
            print(current.value)
            self._inorder_print_tree(current.right)

    def is_bst_satisfied(self):
        if self.root:
            is_bst_satisfied = self._is_bst_satisfied(self.root)
            if is_bst_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, current):
        if current.left:
            if current.value > current.left.value:
                self._is_bst_satisfied(current.left)
            else:
                return False
        if current.right:
            if current.value < current.right.value:
                self._is_bst_satisfied(current.right)
            else:
                return False



bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())

#bst.inorder_print_tree()
#tree.inorder_print_tree()

#print(bst.find(6))

#print(tree.size_(tree.root))

#

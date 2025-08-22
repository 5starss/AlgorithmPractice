class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if not self.root:
            self.root = node
            return
        parent = None
        current = self.root
        while current:
            parent = current
            if current.data < node.data:
                current = current.right
            else:
                current = current.left

        if parent.data < node.data:
            parent.right = node
        else:
            parent.left = node

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
        print()

    def inorder(self, node):
        if node:
            self.preorder(node.left)
            print(node.data, end=' ')
            self.preorder(node.right)
        print()

    def preorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data, end=' ')
        print()

    def preorder(self, node):
        q = [node]

        while q:
            node = q.pop(0)
            print(node.data, end=' ')

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()


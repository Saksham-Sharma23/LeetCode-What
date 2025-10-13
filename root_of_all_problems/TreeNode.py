class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


    def insert_left(self, value):
        if self.left is None:
            self.left = TreeNode(value)


    def insert_right(self, value):
        if self.right is None:
            self.right = TreeNode(value)

    def preorder(self):

        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

a.preorder()
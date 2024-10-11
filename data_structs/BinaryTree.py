class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        # Go all the way left first
        inorder_traversal(root.left)
        # Print the data
        print(root.data)
        # Go all the way right
        inorder_traversal(root.right)

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder traversal
inorder_traversal(root)

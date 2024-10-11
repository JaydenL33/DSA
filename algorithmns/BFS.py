# Node class for the binary tree
import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function for BFS traversal 
def bfs(root: TreeNode):
    returnList = list()
    if root is None:
        return
    # Creating the queue
    queue = collections.deque()
    # Adding the root node to the queue
    queue.append(root)
    while queue:
        qLen = len(queue)
        for i in range(qLen):
            topNode = queue.popleft()
            if topNode:
                returnList.append(topNode.value)
                queue.append(topNode.left)
                queue.append(topNode.right)
    return returnList

               

# Example usage (building the tree)
if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Call bfs on the root node (implementation required)
    print(bfs(root))

# Better solution

import collections

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function for BFS traversal
def bfs(root: TreeNode):
    if root is None:
        return []
    
    return_list = []
    queue = collections.deque([root])  # Initialize the queue with the root node
    
    while queue:
        queue_length = len(queue)
        
        for _ in range(queue_length):
            current_node = queue.popleft()  # Pop the leftmost node from the queue
            return_list.append(current_node.value)
            
            # Add children to the queue if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return return_list


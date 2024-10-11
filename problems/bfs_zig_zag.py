# Node class for the binary tree
import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function for BFS traversal 
def bfs(root: TreeNode):
    currentLevel = 0
    returnList = list()
    if root is None:
        return
    # Creating the queue
    queue = collections.deque()
    # Adding the root node to the queue
    queue.append(root)
    while queue:
        currentLevel += 1
        levelList = list()
        qLen = len(queue)
        for i in range(qLen):
            topNode = queue.popleft()
            if topNode:
                levelList.append(topNode.value)
                queue.append(topNode.left)
                queue.append(topNode.right)
        if (currentLevel % 2 == 0 and topNode):
            levelList.reverse()
            returnList.append(levelList)
        elif (topNode):
            returnList.append(levelList)
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

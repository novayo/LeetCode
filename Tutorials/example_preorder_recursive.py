class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build Tree
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeI = Node('I')
nodeJ = Node('J')
nodeK = Node('K')
nodeL = Node('L')

nodeA.left, nodeA.right = nodeB, nodeC
nodeB.left, nodeB.right = nodeD, nodeE
nodeC.left, nodeC.right = nodeF, nodeG
nodeD.left, nodeD.right = nodeH, nodeI
nodeE.left, nodeE.right = nodeJ, nodeK
nodeF.left = nodeL


# Preorder Traversal - make sure our tree is right
root = nodeA

def dfs(node):
    if not node:
        return
    # visit
    print(node.val)
    dfs(node.left)
    dfs(node.right)

dfs(root)

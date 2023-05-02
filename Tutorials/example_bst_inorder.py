class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build BST
node10 = Node(10)
node20 = Node(20)
node30 = Node(30)
node35 = Node(35)
node45 = Node(45)
node50 = Node(50)
node59 = Node(59)
node60 = Node(60)
node70 = Node(70)
node85 = Node(85)
node100 = Node(100)
node105 = Node(105)

node50.left, node50.right = node30, node70
node30.left, node30.right = node20, node45
node70.left, node70.right = node60, node100
node20.left = node10
node45.left = node35
node60.left = node59
node100.left, node100.right = node85, node105


# Inorder Traversal - make sure our tree is right
node = node50


def iterative(node):
    ans = []
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans


def recursive(node):
    ans = []

    def helper(node):
        nonlocal ans
        if not node:
            return
        helper(node.left)
        ans.append(node.val)
        helper(node.right)

    helper(node)
    return ans


def morris(node):
    ans = []
    while node:
        if not node.left:
            ans.append(node.val)
            node = node.right
        else:
            predecessor = node.left
            while predecessor.right and predecessor.right != node:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                ans.append(node.val)
                node = node.right
    return ans


print(iterative(node50))
#print(recursive(node50))
#print(morris(node50))

root = node50

def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
# preorder(root)

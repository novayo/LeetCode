class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build BST
node20 = Node(20)
node30 = Node(30)
node40 = Node(40)
node50 = Node(50)
node60 = Node(60)
node70 = Node(70)
node80 = Node(80)

node50.left, node50.right = node30, node70
node30.left, node30.right = node20, node40
node70.left, node70.right = node60, node80

root = node50

def recr(node, target):
  if not node:
    return None
  
  if node.val == target:
    if node.left:
      n = node.left
      while n and n.right:
        n = n.right
      return n.val
    else:
      return None
  elif node.val < target:
    n = recr(node.right, target)
    return n if n else node.val
  else:
    return recr(node.left, target)

for v in [20, 30, 40, 50, 60, 70, 80]:
  print(f"predecessor({v}): {recr(root, v)}")

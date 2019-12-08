# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Basic Idea - using bfs
        # pop two items
        # check if first node left == second node right && second node left == first node right
        # append first node left, second node right, first node right, second node left
        
        def BFS(node):
            treeNodeQueue = collections.deque()
            
            if node.left.val != node.right.val: return False
            treeNodeQueue.append(node.left)
            treeNodeQueue.append(node.right)

            while treeNodeQueue:
                firstNode = treeNodeQueue.popleft()
                secondNode = treeNodeQueue.popleft()
                
                if  (firstNode.left == None == secondNode.right) and\
                    (firstNode.right == None == secondNode.left):
                    continue
                elif (firstNode.left == None == secondNode.right) and\
                     (firstNode.right != None and secondNode.left != None) and\
                     (firstNode.right.val == secondNode.left.val):
                    treeNodeQueue.append(firstNode.right)
                    treeNodeQueue.append(secondNode.left)
                elif (firstNode.right == None == secondNode.left) and\
                     (firstNode.left != None and secondNode.right != None) and\
                     (firstNode.left.val == secondNode.right.val):
                    treeNodeQueue.append(firstNode.left)
                    treeNodeQueue.append(secondNode.right)
                elif (firstNode.left != None and secondNode.right != None) and\
                     (firstNode.left.val == secondNode.right.val) and\
                     (firstNode.right != None and secondNode.left != None) and\
                     (firstNode.right.val == secondNode.left.val):
                    treeNodeQueue.append(firstNode.left)
                    treeNodeQueue.append(secondNode.right)
                    treeNodeQueue.append(firstNode.right)
                    treeNodeQueue.append(secondNode.left)
                else:
                    return False
            return True
        
        if root == None or (root.left == root.right == None): return True
        elif root.left == None or root.right == None: return False
        else: return BFS(root)

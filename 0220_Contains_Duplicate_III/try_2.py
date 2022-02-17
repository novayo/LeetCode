class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class BST:
    def __init__(self, t):
        self.root = None
        self.t = t
    
    def add(self, val):
        
        def build(root, val):
            if not root:
                return Node(val)
            
            if root.val > val:
                root.left = build(root.left, val)
            else:
                root.right = build(root.right, val)
            return root
        
        self.root = build(self.root, val)
    
    def isMatch(self, val):
        diff = float('inf')
        root = self.root
        
        while root:
            diff = min(diff, abs(root.val - val))
            
            if diff <= self.t:
                return True
            
            if root.val > val:
                root = root.left
            else:
                root = root.right
                
        return False
        
    
    def remove(self, val):
        '''
        case1 => node has no children => delete node
        case2 => node has one children => replace node by children
        case3 => node has two children => find predecessor and replace node by it
        '''
        def isRoot(node):
            return self.root == node
        
        preNode = None
        node = self.root
        
        # find node
        while node and node.val != val:
            preNode = node
            if node.val > val:
                node = node.left
            else:
                node = node.right
        
        # return if no match
        if not node:
            return
        
        # case1
        if not node.left and not node.right:
            if isRoot(node):
                self.root = None
            else:
                if preNode.left == node:
                    preNode.left = None
                else:
                    preNode.right = None
        
        # case2
        elif not node.left:
            if isRoot(node):
                self.root = node.right
            else:
                if preNode.left == node:
                    preNode.left = node.right
                else:
                    preNode.right = node.right
        elif not node.right:
            if isRoot(node):
                self.root = node.left
            else:
                if preNode.left == node:
                    preNode.left = node.left
                else:
                    preNode.right = node.left
        
        # case3
        else:
            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right
            
            tmp = predecessor.val
            self.remove(predecessor.val)
            node.val = tmp

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        tree = BST(t)
        
        l = 0
        for r, num in enumerate(nums):
            if tree.isMatch(num):
                return True
            
            tree.add(num)
            if r-l >= k:
                tree.remove(nums[l])
                l += 1
        
        return False
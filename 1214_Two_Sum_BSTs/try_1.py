# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        ans1 = set()
        def search1(head):
            if not head:
                return
            search1(head.left)
            search1(head.right)
            ans1.add(head.val)
           
        ans2 = collections.deque()
        def search2(head):
            if not head:
                return False
            search2(head.left)
            search2(head.right)
            ans2.append(head.val)
        
        search1(root1)
        search2(root2)
        for v in ans2:
            if target-v in ans1:
                return True
        return False`

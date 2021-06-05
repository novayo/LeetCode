# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        # 用 inorder 由小到大取得BST的值
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # 因為是balance, 因此取中間的當頭即可
        def build(arr, left, right):
            if left > right:
                return None
            
            mid = (right - left) // 2 + left
            root = TreeNode(arr[mid])
            root.left = build(arr, left, mid-1)
            root.right = build(arr, mid+1, right)
            return root
            
        arr = inorder(root) # 取得 sorted arr
        return build(arr, 0, len(arr)-1) # build tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

    def next(self) -> int:
        ret = -1
        while ret == -1:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                self.root = self.stack.pop()
                ret = self.root.val
                self.root = self.root.right
        return ret

    def hasNext(self) -> bool:
        return self.stack or self.root


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur_level = collections.deque([[self.root, True]])
        self.next_level = collections.deque()
        
        while True:
            node, isLeft = self.cur_level[0]
            
            if isLeft:
                if node.left:
                    self.cur_level[0][1] = False
                    self.next_level.append([node.left, True])
                else:
                    break
            else:
                if node.right:
                    self.cur_level.popleft()
                    self.next_level.append([node.right, True])
                else:
                    break
            
            if not self.cur_level:
                self.cur_level = self.next_level
                self.next_level = collections.deque()

    def insert(self, val: int) -> int:
        node, isLeft = self.cur_level[0]
        if isLeft:
            node.left = TreeNode(val)
            self.cur_level[0][1] = False
            self.next_level.append([node.left, True])
        else:
            node.right = TreeNode(val)
            self.cur_level.popleft()
            self.next_level.append([node.right, True])
        
        if not self.cur_level:
            self.cur_level = self.next_level
            self.next_level = collections.deque()
        
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
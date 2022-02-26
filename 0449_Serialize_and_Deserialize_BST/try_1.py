# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from binascii import hexlify, unhexlify

class Codec:
    
    def preorder(self, node, container):
        if not node:
            return
        container.append(str(node.val))
        self.preorder(node.left, container)
        self.preorder(node.right, container)
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ret = []
        self.preorder(root, ret)
        return hexlify(','.join(ret).encode()).decode()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        data = unhexlify(data).decode()
        
        preorder = [int(x) for x in data.split(',')]
        n = len(preorder)
        
        # next bigger
        bigger = {}
        stack = []
        for i, v in enumerate(preorder):
            while stack and stack[-1] < v:
                bigger[stack.pop()] = i
            stack.append((v))
        while stack:
            bigger[stack.pop()] = n
        
        index_preorder = 0
        def recr(left, right):
            nonlocal index_preorder
            if left > right:
                return None
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if left != right:
                index = bigger[root.val]
                root.left = recr(left+1, index-1)
                root.right = recr(index, right)
            return root
        
        return recr(0, len(preorder)-1)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

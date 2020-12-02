# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''
        bfs
        '''
        if not root:
            return ""
        ret = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            
            if not node:
                ret.append("null")
            else:
                ret.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        ret = data.split(",")

        root = TreeNode(int(ret[0]))
        queue = collections.deque()
        queue.append(root)
        
        i = 1
        while queue and i < len(ret):
            node = queue.popleft()
            
            if ret[i] != "null":
                node.left = TreeNode(int(ret[i]))
                queue.append(node.left)
            i += 1
            if ret[i] != "null":
                node.right = TreeNode(int(ret[i]))
                queue.append(node.right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
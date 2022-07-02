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
        ret = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                ret.append("null")
            else:
                ret.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        while ret and ret[-1] == 'null':
            ret.pop()
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        data = data.split(',')
        
        root = TreeNode(data[0])
        que = collections.deque([root])
        i = 1
        while que and i < len(data):
            node = que.popleft()
            
            if data[i] != 'null':
                node.left = TreeNode(data[i])
                que.append(node.left)
                
            i += 1
            if i < len(data) and data[i] != 'null':
                node.right = TreeNode(data[i])
                que.append(node.right)
            i += 1
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(lambda: [None, None, None])  # [left, right, parent]

        # build graph
        def preorder(node, parent):
            if not node:
                return
            graph[node.val][0] = node.left.val if node.left else None
            graph[node.val][1] = node.right.val if node.right else None
            graph[node.val][2] = parent
            preorder(node.left, node.val)
            preorder(node.right, node.val)

        preorder(root, None)

        # bfs
        cache = set()
        que = collections.deque()

        # init
        que.append((startValue, ''))

        # loop
        while que:
            next_que = collections.deque()
            for nodeValue, cur_path in que:
                if nodeValue == destValue:
                    return cur_path
                if nodeValue in cache:
                    continue
                cache.add(nodeValue)

                node = graph[nodeValue]

                if node[2]:
                    next_que.append((node[2], cur_path + 'U'))
                if node[0]:
                    next_que.append((node[0], cur_path + 'L'))
                if node[1]:
                    next_que.append((node[1], cur_path + 'R'))
            que = next_que
        return ''

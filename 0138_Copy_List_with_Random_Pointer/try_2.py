"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        先把原本的node前面都 複製一個自己 O(n)
        之後再把random給 複製的自己 O(n)
        最後把複製的串起來即可 O(n)
        
        time complexity: O(n)
        space complexity: O(n)
        '''
        
        def printAll(node):
            while node:
                print(node.val, end=" -> ")
                node = node.next
            print()
            
        if not head:
            return None
        
        # 複製一個自己
        tmp = head
        while tmp:
            newNode = Node(tmp.val)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        
        # 複製random到 next
        tmp = head
        while tmp and tmp.next:
            tmp.next.random = None if tmp.random == None else tmp.random.next
            tmp = tmp.next.next
        # printAll(head.next)
        
        # 拿到複製的
        tmp = head.next
        while tmp and tmp.next:
            tmp.next = tmp.next.next
            tmp = tmp.next
        # printAll(head.next)
        
        
        return head.next

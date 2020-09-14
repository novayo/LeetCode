# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        先找到底，讓尾巴接上頭
        之後再去算 新的尾巴在哪：第 n- k%n -1個
        之後讓這個位置變成尾巴，下一個變成頭即可
        '''
        
        if not head:
            return None
        
        # 讓尾巴接上頭
        length = 1
        tmp = head
        while tmp.next:
            length += 1
            tmp = tmp.next
        tmp.next = head
        
        # 數新的尾巴在哪
        k1 = length- k%length -1
        
        # 找到新尾巴，並更新成尾巴，下一個為頭
        tmp = head
        for _ in range(k1):
            tmp = tmp.next
        
        newHead = tmp.next
        tmp.next = None
        
        return newHead

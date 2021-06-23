# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        
        def print_():
            tmp = newHead
            while tmp:
                print(tmp.val, end=' -> ')
                tmp = tmp.next
            print()
            
        # 先找到左邊的頭
        preHead = newHead
        leftHead = head
        cur = 1
        while cur < left:
            leftHead = leftHead.next
            preHead = preHead.next
            cur += 1
        
        # 開始丟到頭
        preLeftHead = preHead
        curHead = leftHead.next
        preHead = leftHead
        while cur < right:
            preHead.next = curHead.next
            curHead.next = leftHead
            preLeftHead.next = curHead
            leftHead = preLeftHead.next
            curHead = preHead.next
            cur += 1
            # print_()
            
        return newHead.next
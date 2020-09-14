# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        1. 先跑一遍，拿到長度 O(n) O(1) => length
        2. 並跟k拿到餘數（實際要移的長度）=> k1
        
        3. 從第length-k1-1個開始reverse k1個 list（一直往頭那邊丟）O(k1) O(1)
        4. 再從頭開始 reverse k1-1 個 list O(k1) O(1)
        
        eg. 1->2->3->4->5->NULL, k = 2
        1. length = 5
        2. k1 = 2%5 = 5
        3. 5->4-> 1->2->3->NULL
        4. 4->5-> 1->2->3->NULL
        
        time complexity: O(n)
        space complexity: O(1)
        '''
        
        def printAll(node):
            while node:
                print(node.val, end=" -> ")
                node = node.next
            print()
        
        if not head:
            return None
        
        # 拿到長度
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        
        # 拿到要翻轉的長度
        k1 = k % length
        
        # 第一次reverse
        ## 走到第length-k1-1個node
        tmp = head
        for _ in range(length-k1-1):
            tmp = tmp.next
        
        ## reverse
        while tmp.next:
            nextNode = tmp.next
            tmp.next = nextNode.next
            nextNode.next = head
            head = nextNode
        
        # 第二次reverse
        tmp = head
        for _ in range(k1-1):
            # printAll(head)
            nextNode = tmp.next
            tmp.next = nextNode.next
            nextNode.next = head
            head = nextNode
        
        return head

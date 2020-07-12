# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) O(1)
        '''
        用龜兔賽跑找到中間，並將其看成"前list"與"後list"
        將"前list" reverse後，看是否與後list相同
        
        然後再龜兔賽跑的過程中可以邊reverse list
        '''
        
        fast = slow = head
        pre = None
        
        while fast and fast.next:
            fast = fast.next.next
            
            # reverse：Leetcode 206
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        
        # 如果是偶數個，1->2->2->1->None
        # 此時的 list 長 1<-2 2->1
        # fast會抓到None，pre會抓到第一個2，slow會抓到第二個2
        #
        # 如果是奇數個，1->2->3->2->1->None
        # 此時的 list 長 1<-2 3->2->1
        # fast會抓到1，pre會抓到第一個2，slow會抓到3
        # 那3是因為總長度是奇數所以不用比較，因此如果有fast，代表是奇數個，則要讓slow往後一格
        if fast:
            slow = slow.next
        
        while slow:
            if pre.val != slow.val:
                return False
            else:
                pre = pre.next
                slow = slow.next
        return True

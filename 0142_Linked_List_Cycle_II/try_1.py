# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # tortoise and the hare
        '''
        這就是一個特性，
        O -> O -> O -> O -> X
                       |    |
                       O <- O
        
        未進入cycle前，走的路徑為 F
        假設相遇的點為X，而在cycle內走了 a 後相遇
        剩下cycle的距離就為 C - a （C為cycle長度）
        
        第一次走
        tortoise跟hare同時走，相遇時，由於速度差是兩倍，
        故此時 2 * (F + a) = F + a + nC    =>   烏龜走了F+a的距離，此時的兔子走了F+a外加不知道走了幾圈(nC)
        就可知 nC - a = F
        
        第二次走
        此時讓烏龜從新走，
        ** 使烏龜跟兔子走一樣的速度 **
        當烏龜走到cycle點時，烏龜走了F
        而 F 剛好又等於 nC - a = C - a + (n-1)C   =>   表示 兔子又走了C - a 外加不知道走了幾圈(nC)
        而這個C - a剛好就是剩下cycle的距離（第18行）
        所以第二次這樣走，剛好能在cycle的起始點相遇
        '''
        
        if head == None or head.next == None:
            return None
        
        tortoise = head
        hare = head
        
        # 第一次走
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                break
        
        if tortoise != hare:
            return None
        
        
        # 第二次走
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        
        return tortoise

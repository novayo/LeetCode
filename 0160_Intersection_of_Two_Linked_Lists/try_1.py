# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        a往下跑A，b往下跑B
        但是 A跟B的長度可能不同
        因此，讓a走完之後走B，讓b走完之後走a，在這之中去看是否有相同的node即可
        
        原理是因為
        a走完A之後走B，b走完B之後走A，
        就代表讓a走了A+B，b也走了A+B，此時的長度就都走得一樣了
        
        換句話說
        就是讓 左圖的 B折上去A的前面，讓A折下來B的前面
        A: "b1->b2->b3"->a1->a2
        B: "a1->a2"->b1->b2->b3
        
        這樣就轉換題目成長度相同的兩個linkedlist去跑了
        '''
        if headA == [] or headB == []:
            return 0
        
        heada = headA
        headb = headB
        
        while heada != headb:
            heada = headB if not heada else heada.next
            headb = headA if not headb else headb.next
        return heada

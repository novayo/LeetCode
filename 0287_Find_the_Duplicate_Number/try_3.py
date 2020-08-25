class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 龜兔賽跑（Floyd's Tortoise and Hare）
        '''
        先將list看成linked list
        
        則 [1,3,4,2,2] 會變成 
        (值是1，則連到index=1的值，
         值是3，則連到index=3的值.....)
        1 -> 3 -> 2 -> 4
                  ^----|
        
        此時可以發現會有cycle（重複的點會是cycle入口）
        
        https://i.imgur.com/aICrcya.png
        假設黃色的點為相遇的點，而速度上又是 2(烏龜) = 兔子
        所以等式可以寫成 2*(F+a) = F + a + nC
        因此可以導出 F = nC - a，則因為nC是跑了幾圈，會回到原處
        故可以將n帶成1，可得到 F = C - a
        
        所以其實C - a走的長度跟 F 是一樣的，
        因此在第一次相遇之後，
        讓烏龜跟兔子的速度一樣，烏龜再重新走一次，而兔子繼續走
        下一次的相遇點就會是cycle的入口，也就會是我們要的答案
        '''
        
        tortoise = nums[0]
        hare = nums[0]
        
        # 第一次相遇
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # 第二次相遇
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise
            

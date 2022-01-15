class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # cost - gas => [-2, -2, -2, 3, 3]
        # 左右兩邊，看從哪裡開始分割，左邊<=右邊 & 起始位置>=0
        subs = []
        for g, c in zip(gas, cost):
            subs.append(g-c)
        
        
        # [-4, -3, 1, 3, 3]
        found = set()
        find_start = False
        count = 0
        i = j = 0
        while find_start == False or i != j:
            if find_start:
                count += subs[i]
                if count < 0:
                    find_start = False
                    count = 0
            else:
                if i in found:
                    return -1
                else:
                    found.add(i)
                    
                if subs[i] >= 0:
                    j = i
                    count = subs[i]
                    find_start = True
            i += 1
            if i >= len(subs):
                i = 0
        return i

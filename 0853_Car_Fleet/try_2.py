class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time_list = []
        
        for pos, spd in zip(position, speed):
            pos_time_list.append((pos, (target-pos) / spd))
        
        pos_time_list.sort()
        
        
        ans = 0
        cur_top = pos_time_list[-1][1]
        for i in range(len(pos_time_list)-2, -1, -1):
            if pos_time_list[i][1] > cur_top:
                ans += 1
                cur_top = pos_time_list[i][1]
        
        return ans + 1
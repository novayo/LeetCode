class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ''' 用距離排序(因為不能超車)，計算每個人的到達時間點
            後面的人到達的時間點
                如果小於等於前面的人 => 會疊在一起
                如果大於前面的人 => 則可以算一台
        '''
        pack = sorted(zip(position, speed), reverse=True)
        
        ans = 0
        cur_max = 0
        for pos, spd in pack:
            time = (target-pos) / spd
            
            if time > cur_max:
                ans += 1
                cur_max = time
        return ans

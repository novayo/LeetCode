class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''
        Greedy
        
        能抱大腿就抱大腿
        不能抱大腿就出來創業
        '''
        
        counter = collections.Counter(nums)
        seq = collections.defaultdict(int)  # key: ending number, val: 個數
        
        for num in nums:
            if counter[num] == 0:
                continue
            
            # 抱大腿
            if seq[num-1] > 0:
                seq[num-1] -= 1
                seq[num] += 1
                counter[num] -= 1
            else:
                if counter[num+1] > 0 and counter[num+2] > 0:
                    # 出來創業
                    seq[num+2] += 1
                    counter[num] -= 1
                    counter[num+1] -= 1
                    counter[num+2] -= 1
                else:
                    return False
        return True
        

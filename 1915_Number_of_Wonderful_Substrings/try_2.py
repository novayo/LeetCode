class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def need_continue(total_dict, tmp_dict):
            count = 0
            for k, v in tmp_dict.items():
                if v % 2 == 1 and total_dict[k] <= v:
                    count += 1
                    if count > 1:
                        return False
            return True
        
        def match(tmp_dict):
            count = 0
            for k, v in tmp_dict.items():
                if v % 2 == 1:
                    count += 1
                    if count > 1:
                        return False
            return True
                        
        ans = 0
        n = len(word)
        dp = collections.defaultdict(int)
        
        for i in range(n):
            tmp = collections.defaultdict(int)
            dp[word[i]] += 1
            for j in range(i, -1, -1):
                tmp[word[j]] += 1
                
                if need_continue(dp, tmp):
                    if match(tmp):
                        ans += 1
                else:
                    break
        return ans
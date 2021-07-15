class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ans = ''
        appear = [0] * len(order)
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        
        for s in str:
            if s in order_dict:
                appear[order_dict[s]] += 1
            else:
                ans += s
        
        for i, times in enumerate(appear):
            ans += order[i] * times
        return ans
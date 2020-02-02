class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = -float('inf')
        basket = set()
        i = j = 0
        is_first = True
        while i < len(tree):
            basket.add(tree[i])
            if is_first:
                j = i
                is_first = False
            elif len(basket) > 2:
                ans = max(ans, i-j)
                i = j
                basket.clear()
                is_first = True
                
                flag = False
                while i < len(tree) and tree[i] == tree[i-1]:
                    i += 1
                    flag = True
                if flag:
                    continue
            i += 1
        ans = max(ans, i-j)
        return ans

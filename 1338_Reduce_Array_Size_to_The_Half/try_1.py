class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        ans = sum = 0
        for key in sorted(counter, key=counter.get, reverse=True):
            sum += counter[key]
            ans += 1
            if sum*2 >= len(arr):
                break
        return ans
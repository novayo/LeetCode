class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for n in nums:
            if n in found:
                return True
            else:
                found.add(n)
        return False

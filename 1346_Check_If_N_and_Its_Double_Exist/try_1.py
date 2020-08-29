class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # using set
        found = set()
        for a in arr:
            if a / 2 in found or 2 * a in found:
                return True
            else:
                found.add(a)
        return False

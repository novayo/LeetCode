class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) <= 1 or len(B) <= 1: return 0
        ans = float('inf')
        reverse = 0
        
        while reverse < 2:
            if reverse == 1:
                A, B = B, A
            countA = collections.Counter(A)
            countB = collections.Counter(B)

            for key, value in countA.items():
                num_for_changed = len(A)-value
                value_in_B = countB.get(key)
                if value_in_B == None or value_in_B < num_for_changed: continue

                tmp = 0
                for i, a in enumerate(A):
                    if a != key:
                        if B[i] == key:
                            tmp += 1
                if tmp < num_for_changed: continue
                ans = min(ans, num_for_changed)
                break
            reverse += 1
        return ans if ans != float('inf') else -1

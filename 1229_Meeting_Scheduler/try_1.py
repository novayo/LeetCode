class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        n1 = len(slots1)
        n2 = len(slots2)

        i = j = 0
        while i < n1 and j < n2:
            startI, endI = slots1[i]
            startJ, endJ = slots2[j]

            if startI >= endJ:
                j += 1
            elif startJ >= endI:
                i += 1
            else:
                start = max(startI, startJ)
                end = min(endI, endJ)
                intersect = end - start

                if intersect >= duration: 
                    return [start, start+duration]
                else:
                    if endI >= endJ:
                        j += 1
                    else:
                        i += 1

        return []
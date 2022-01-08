class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        '''
        memo = {}
        recursive (jug1=0, jug2=0)
            -> fill 1
            -> fill 2
            -> clear 1
            -> clear 2
            -> Poor 1 to 2
            -> Poor 2 to 1
            
            if one of them True => return True
            else => return False
        '''
        
        found = set()
        queue = set()
        
        queue.add((0, 0))
        while queue:
            jug1, jug2 = queue.pop()
            
            if jug1 == targetCapacity or jug2 == targetCapacity or jug1+jug2 == targetCapacity:
                return True
            
            for new_1, new_2 in [jug1Capacity, jug2], [jug1, jug2Capacity], [0, jug2], [jug1, 0], [max(jug1 - (jug2Capacity-jug2), 0), min(jug2 + jug1, jug2Capacity)], [min(jug1 + jug2, jug1Capacity), max(jug2 - (jug1Capacity-jug1), 0)]:
                if (new_1, new_2) not in found:
                    found.add((new_1, new_2))
                    queue.add((new_1, new_2))
        
        return False

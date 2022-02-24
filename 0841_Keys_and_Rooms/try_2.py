class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        
        keys |= set(rooms[0])
        visited = set([0])
        
        while keys:
            key = keys.pop()
            
            if key in visited:
                continue
            
            visited.add(key)
            keys |= set(rooms[key])
            
            if len(visited) == len(rooms):
                return True
        
        return False

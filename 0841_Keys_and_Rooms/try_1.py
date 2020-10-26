class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        visited = set()
        visited.add(0)
        
        queue = collections.deque()
        for key in rooms[0]:
            queue.append(key)
            keys.add(key)
        
        while queue:
            if len(visited) >= len(rooms):
                break
                
            key = queue.popleft()
            
            if key in visited:
                continue
            else:
                visited.add(key)
                for k in rooms[key]:
                    queue.append(k)
                    keys.add(k)
        
        return len(visited) == len(rooms)

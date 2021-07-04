class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        ans = [-1] * len(cars)
        nodes = []
        heap = []
        
        for i in range(len(cars)-1):
            cur_pos, cur_spd = cars[i]
            next_pos, next_spd = cars[i+1]
            nodes.append(Node(i-1, i, i+1))
            
            if cur_spd <= next_spd:
                heapq.heappush(heap, (-1, i, i+1))
            else:
                heapq.heappush(heap, ((next_pos-cur_pos)/(cur_spd-next_spd), i, i+1))
        
        nodes.append(Node(len(cars)-2, len(cars)-1, len(cars)))
        
        while heap:
            collide_time, index, _next = heapq.heappop(heap)
            pre = nodes[index].pre
            next = nodes[index].next
            
            if nodes[index].next != _next: 
                continue
            
            if collide_time != -1:
                ans[index] = round(collide_time, 5)
                nodes[pre].next = next
                nodes[_next].pre = pre
                if pre >= 0 and cars[pre][1] > cars[next][1]:
                    cur_pos, cur_spd = cars[pre]
                    next_pos, next_spd = cars[next]
                    heapq.heappush(heap, ((next_pos-cur_pos)/(cur_spd-next_spd), pre, next))
        return ans

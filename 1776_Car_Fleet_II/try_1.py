class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        hit_time = [-1] * len(cars)
        heap = []
        index_minus_1 = len(cars)-1
        i = len(cars)-2
        
        while i >= 0:
            target = i+1
            cur_pos, cur_spd = cars[i]
            next_pos, next_spd = cars[target]
            next_hit_time = hit_time[target]
            max_pos, max_spd = cars[index_minus_1]
            
            update_time = 0
            
            while True:
                if cur_spd <= next_spd:
                    if next_hit_time == -1:
                        update_time = -1
                        heap = []
                        index_minus_1 = i
                        break
                    else:
                        target += 1
                        next_pos, next_spd = cars[target]
                        next_hit_time = hit_time[target]
                elif cur_spd > next_spd:
                    max_hit_time = (max_pos-cur_pos) / (cur_spd-max_spd)
                    if not heap or -heap[0][0] <= max_hit_time:
                        update_time = max_hit_time
                        break
                    
                    cur_hit_time = (next_pos-cur_pos) / (cur_spd-next_spd)
                    if next_hit_time == -1:
                        update_time = cur_hit_time
                        break
                    else:
                        if cur_hit_time <= next_hit_time:
                            update_time = cur_hit_time
                            break
                        else:
                            target += 1
                            next_pos, next_spd = cars[target]
                            next_hit_time = hit_time[target]
            heapq.heappush(heap, (-update_time, i))
            hit_time[i] = round(update_time, 5)
            i -= 1
        return hit_time

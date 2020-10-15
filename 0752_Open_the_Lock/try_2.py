class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        bi-bfs
        '''
        
        deadends = set(deadends)
        
        queue_start = collections.deque()
        queue_start.append((0,0,0,0,0))
        dict_start = {}
        
        queue_end = collections.deque()
        queue_end.append((int(target[0]), int(target[1]), int(target[2]), int(target[3]), 0))
        dict_end = {}
        
        while queue_start and queue_end:
            if len(queue_start) > len(queue_end):
                queue_start, queue_end = queue_end, queue_start
                dict_start, dict_end = dict_end, dict_start
            
            i1, i2, i3, i4, count = queue_start.popleft()
            
            s = str(i1) + str(i2) + str(i3) + str(i4)
            
            if s in dict_end:
                return count + dict_end[s]
            elif s in dict_start or s in deadends:
                continue
            
            dict_start[s] = count
            for i,j,k,l in [(i1+1)%10, i2, i3, i4], [(i1-1)%10, i2, i3, i4],\
                           [i1, (i2+1)%10, i3, i4], [i1, (i2-1)%10, i3, i4],\
                           [i1, i2, (i3+1)%10, i4], [i1, i2, (i3-1)%10, i4],\
                           [i1, i2, i3, (i4+1)%10], [i1, i2, i3, (i4-1)%10]:
                if str(i) + str(j) + str(k) + str(l) not in dict_start:
                    queue_start.append((i, j, k, l, count+1))
        
        return -1
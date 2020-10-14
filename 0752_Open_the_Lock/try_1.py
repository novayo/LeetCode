class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque()
        queue.append((0,0,0,0,0))
        visited = set(deadends)
        ans = float('inf')
        
        while queue:
            i1, i2, i3, i4, count = queue.popleft()
            
            s = str(i1)+str(i2)+str(i3)+str(i4)
            
            if s in visited:
                continue
            
            visited.add(s)
            
            if s == target:
                return count
            else:
                for i,j,k,l in [(i1+1)%10,i2,i3,i4],[(i1-1)%10,i2,i3,i4],\
                               [i1,(i2+1)%10,i3,i4],[i1,(i2-1)%10,i3,i4],\
                               [i1,i2,(i3+1)%10,i4],[i1,i2,(i3-1)%10,i4],\
                               [i1,i2,i3,(i4+1)%10],[i1,i2,i3,(i4-1)%10]:
                    if str(i)+str(j)+str(k)+str(l) not in visited:
                        queue.append((i,j,k,l,count+1))
                    
        return -1

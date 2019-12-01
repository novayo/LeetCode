class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ans, queue = set(), collections.deque(range(10))
        
        while queue:
            n1 = queue.popleft()
            if low <= n1 <=high:
                ans.add(n1)
            
            if n1 < high:
                if n1%10 == 0:
                    queue.append(n1*10+1)
                elif n1%10 == 9:
                    queue.append(n1*10+8)
                else:
                    queue.append(n1*10+n1%10-1)
                    queue.append(n1*10+n1%10+1)
        return sorted(ans)

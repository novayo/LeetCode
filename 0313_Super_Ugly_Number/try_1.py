class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        dp = [1]
        index_of_primes = [0] * len(primes)
        
        visited = set()
        heap = []
        for i in range(len(primes)):
            candidate = dp[index_of_primes[i]] * primes[i]
            heapq.heappush(heap, (candidate, i))
            visited.add(candidate)
        
        for _ in range(n-1):
            lower, i = heapq.heappop(heap)
            
            dp.append(lower)
            index_of_primes[i] += 1
            
            candidate = dp[index_of_primes[i]] * primes[i]
            while candidate in visited:
                index_of_primes[i] += 1
                candidate = dp[index_of_primes[i]] * primes[i]
            
            heapq.heappush(heap, (candidate, i))
            visited.add(candidate)
        
        return dp[n-1]
    

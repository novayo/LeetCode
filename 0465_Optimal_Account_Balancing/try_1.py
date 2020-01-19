class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        hash_table = collections.defaultdict(int)
        for t in transactions:
            hash_table[t[0]] -= t[2]
            hash_table[t[1]] += t[2]
        
        b = sorted([x for x in hash_table.values() if x != 0])
        # print(b)
        
        def dfs(index):
            while index<len(b) and b[index] == 0:
                index+=1
            if index == len(b):
                return 0
            
            r = float('inf')
            for i in range(index+1, len(b)):
                if b[i] + b[index] == 0:
                    b[i] += b[index]
                    tmp = dfs(index+1)
                    r = min(r, 1+tmp)
                    # print("0: ", tmp)
                    b[i] -= b[index]
                    break
                elif b[i] * b[index] < 0:
                    b[i] += b[index]
                    tmp = dfs(index+1)
                    r = min(r, 1+tmp)
                    # print("1: ", tmp)
                    b[i] -= b[index]
            return r
        
        return dfs(0)
    

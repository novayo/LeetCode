class Solution:
    def checkRecord(self, n: int) -> int:
        # O(18n) time / O(1) space
        MOD = pow(10, 9) + 7
        A, P, PA, L1, L1A, L2, L2A = 0,1,2,3,4,5,6
        pre = {A:1, P:1, PA:0, L1:1, L1A:0, L2:0, L2A:0}
        
        for _ in range(n-1):
            new = {A:0, P:0, PA:0, L1:0, L1A:0, L2:0, L2A:0}
            
            new[P] = pre[P] + pre[L1] + pre[L2]
            new[PA] = pre[A] + pre[P] + pre[PA] + pre[L1A] + pre[L2A] + pre[L1] + pre[L2]
            new[L1] = pre[P]
            new[L1A] = pre[A] + pre[PA]
            new[L2] = pre[L1]
            new[L2A] = pre[L1A]
            
            for k in new:
                new[k] %= MOD
            
            pre = new
        
        return sum(pre.values()) % MOD

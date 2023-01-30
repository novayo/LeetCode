class UF:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.roots = 0
    
    # TC: O(1)
    def _exist(self, n1):
        return n1 in self.parents
    
    # TC: O(1)
    def add(self, n1):
        if not self._exist(n1):
            self.parents[n1] = n1
            self.ranks[n1] = 0
            self.roots += 1
    
    # TC: O(logn)
    def findParent(self, n1):
        if n1 != self.parents[n1]:
            self.parents[n1] = self.findParent(self.parents[n1])
        return self.parents[n1]
    
    # TC: O(logn)
    def union(self, n1, n2):
        # 如果有點不存在就跳過
        if not self._exist(n1) or not self._exist(n2):
            return
        
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        
        # 如果是同一棵樹就跳過
        if p1 == p2:
            return
        
        # 合併，所以樹數量-1
        self.roots -= 1
        
        # 合併，比較ranks進行合併
        r1 = self.ranks[p1]
        r2 = self.ranks[p2]
        
        if r1 > r2:
            self.parents[p2] = p1
        elif r1 < r2:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.ranks[p1] += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # init
        tree = UF()
        ans_list = []
        
        # get answer
        for n1 in positions:
            n1 = tuple(n1)
            x, y = n1
            
            # 把點加入樹內
            tree.add(n1)
            
            # 跟周圍合併
            for n2 in (x-1,y), (x+1,y), (x,y-1), (x,y+1):
                tree.union(n1, n2)
            
            # 取得現在有幾棵樹
            ans_list.append(tree.roots)
        
        return ans_list
        

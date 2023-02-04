class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        
        # 從最小的x y開始
        buildings.sort()
        
        # 取得所有的x
        valid_x = set()
        for x1,x2,h in buildings:
            valid_x.add(x1)
            valid_x.add(x2)
        
        ans = []
        maxHeap = []
        i = 0
        for x in sorted(valid_x):
            # 把起點 <= 目前x的加入heap
            while i < n and buildings[i][0] <= x:
                heapq.heappush(maxHeap, (-buildings[i][2], buildings[i][1]))
                i += 1
            
            # 把終點 <= 目前x的加入heap
            while maxHeap and maxHeap[0][1] <= x:
                heapq.heappop(maxHeap)
            
            # 取得答案
            h = -maxHeap[0][0] if maxHeap else 0
            
            # Edges case:
            #     1. 第一個方塊
            #     2. 水平重疊：因為從最小的x y開始，所以只取最左邊高度
            #     3. 垂直重疊：題目不會出現
            if not ans or ans[-1][1] != h:
                ans.append([x, h])
        return ans

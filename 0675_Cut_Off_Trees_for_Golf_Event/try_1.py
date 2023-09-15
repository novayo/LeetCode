class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        '''
        0 => 不能走
        1 => 可以走
        >1=> 有樹

        2500 cells => N

        [
            [54581641,64080174,24346381,69107959],
            [86374198,61363882,68783324,79706116],
            [1,92178815,89819108,94701471],
            [83920491,22724204,46281641,47531096],
            [89078499,18904913,25462145,60813308]]
        
        找此點->下一個目標的座標 的最短距離
        # BFS => N * N => 6.25 * 10^6
        def shortest_path(i1,j1,i2,j2):
            return 最短距離
        '''
        # n*nlogn + 2n + nlogn = 2 * 10 ^ 4
        height, width = len(forest), len(forest[0])

        def shortest_path(i1,j1,i2,j2):
            def get_score(step, x, y):
                return step + abs(i2-x) + abs(j2-y)

            pq = [(get_score(0, i1, j1), 0, i1, j1)] # step, x, y
            done_set = set()

            while pq:
                score, step, x, y = heapq.heappop(pq)
                if x == i2 and y == j2:
                    return step

                if (x, y) in done_set:
                    continue
                done_set.add((x, y))

                for i, j in [x-1,y], [x+1,y], [x,y-1], [x,y+1]:
                    if not (0 <= i < height and 0 <= j < width):
                        continue
                    if forest[i][j] == 0:
                        continue
                    if (i, j) in done_set:
                        continue
                    heapq.heappush(pq, (get_score(step+1, i, j), step+1, i, j))
            return -1

        start_tree_height = forest[0][0]

        # O(n)
        height_arr = []
        for i in range(height):
            for j in range(width):
                height_arr.append((forest[i][j], i, j))
        # O(nlogn)
        height_arr.sort()

        # 從第一棵樹的idx開始
        # O(n)
        idx = 0
        while idx < len(height_arr):
            if height_arr[idx][0] > 1:
                break
            idx += 1
        
        # O(n * n)
        total_steps = 0
        cur_x = cur_y = 0
        while idx < len(height_arr):
            result = shortest_path(
                cur_x,
                cur_y,
                height_arr[idx][1],
                height_arr[idx][2]
            )

            if result == -1:
                return -1

            total_steps += result
            cur_x, cur_y = height_arr[idx][1], height_arr[idx][2]
            forest[cur_x][cur_y] = 1
            idx += 1
        return total_steps

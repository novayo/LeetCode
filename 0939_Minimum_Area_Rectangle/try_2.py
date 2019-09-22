class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 以x軸為主，去建立一個graph
        def buildGraph():
            graph = {}
            for element in points:
                if element[0] in graph:
                    graph[element[0]].add(element[1])
                else:
                    graph[element[0]] = set()
                    graph[element[0]].add(element[1])
            return graph
        
        graph = buildGraph()
        ans = float("inf")
        
        # 找到不同的兩個點（找對角線），如果x1有出現在y2的x上且x2有出現在y1的x上的話，就成立
        for e1 in points:
            for e2 in points[points.index(e1)+1:]:
                if e1[0] != e2[0] and e1[1] != e2[1]:
                    if e1[1] in graph[e2[0]] and e2[1] in graph[e1[0]]:
                        ans = min(ans, abs(e1[0] - e2[0]) * abs(e1[1] - e2[1]))
            
        return 0 if ans == float("inf") else ans

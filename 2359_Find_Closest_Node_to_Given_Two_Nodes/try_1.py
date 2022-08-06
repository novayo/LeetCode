class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        n1_visited = [False] * n
        n2_visited = [False] * n
        
        while node1 > -1 or node2 > -1:
            candidate = []
            if node1 > -1:
                # avoid cycle
                if n1_visited[node1] == True:
                    node1 = -1
                else:
                    n1_visited[node1] = True
                    if n1_visited[node1] == n2_visited[node1] == True:
                        candidate.append(node1)
                    node1 = edges[node1]
            
            if node2 > -1:
                # avoid cycle
                if n2_visited[node2] == True:
                    node2 = -1
                else:
                    n2_visited[node2] = True
                    if n1_visited[node2] == n2_visited[node2] == True:
                        candidate.append(node2)
                    node2 = edges[node2]
            
            if candidate:
                return sorted(candidate)[0]
        return -1
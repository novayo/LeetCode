class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = {}
        
        for i in range(len(equations)):
            a, b = equations[i]
            value= values[i]
            if a not in path:
                path[a] = {}
            if b not in path:
                path[b] = {}
            path[a].update({b:value})
            path[b].update({a:1/value})
        
        def backtrack(a, b, found, anscontainer):
            if a not in path:
                return False
            if b in path[a]:
                if anscontainer[0] == -float('inf'):
                    anscontainer[0] = 1
                anscontainer[0] *= path[a][b]
                return True
            
            found.add(a)
            
            for a_child in path[a]:
                if a_child in found:
                    continue
                if backtrack(a_child, b, found, anscontainer):
                    anscontainer[0] *= path[a][a_child]
                    found.remove(a)
                    return True
            
            found.remove(a)
            return False
        
        ans = []
        for a, b in queries:
            ans_container = [-float('inf')]
            backtrack(a, b, set(), ans_container)
            ans.append(ans_container[0] if ans_container[0] != -float('inf') else -1)
        
        return ans

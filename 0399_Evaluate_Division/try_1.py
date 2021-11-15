class Node:
    def __init__(self):
        self.children = {}
    
    def add(self, node, val):
        self.children.update({node: val})

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_table = {}
        
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]
            
            nodea = node_table.get(a, Node())
            nodeb = node_table.get(b, Node())
            
            nodea.add(nodeb, value)
            nodeb.add(nodea, 1/value)
        
            node_table[a] = nodea
            node_table[b] = nodeb
        
        def backtracking(nodea, nodeb, found, cur):
            cur.append(nodea)
            found.add(nodea)
            
            if nodea == nodeb:
                return True
            
            for node in nodea.children:
                if node in found:
                    continue

                if backtracking(node, nodeb, found, cur):
                    return True

            cur.pop()
            found.remove(nodea)
            return False
                    
        
        ans = []
        for a, b in queries:
            if a not in node_table or b not in node_table:
                ans.append(-1)
            elif a == b:
                ans.append(1)
            else:
                tmp = []
                backtracking(node_table[a], node_table[b], set(), tmp)
                
                if len(tmp) == 0:
                    ans.append(-1)
                else:
                    cur = 1
                    for i in range(len(tmp)-1):
                        cur *= tmp[i].children[tmp[i+1]]
                    ans.append(cur)
        
        return ans

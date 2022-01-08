"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # build tree
        tree = {}
        for employee in employees:
            tree[employee.id] = employee
        
        # sum up
        ans = 0
        queue = []
        queue.append(id)
        while queue:
            node_id = queue.pop()
            node = tree[node_id]
            ans += node.importance
            
            for child in node.subordinates:
                queue.append(child)
        
        return ans
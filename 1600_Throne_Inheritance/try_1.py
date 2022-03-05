class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.table = collections.defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.table[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []
        
        def dfs(x):
            nonlocal curOrder
            
            if x not in self.dead:
                curOrder.append(x)
            
            for child in self.table[x]:
                dfs(child)
        
        dfs(self.kingName)
        return curOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [(nestedList, 0)]
    
    def next(self) -> int:
        List, index = self.stack.pop()
        self.stack.append((List, index+1))
        return List[index]
        
    
    def hasNext(self) -> bool:
        if len(self.stack) == 0:
            return False
        
        # 保證尾巴是數字
        def dfs():
            if not self.stack:
                return
            
            List, index = self.stack[-1]
            
            if index >= len(List):
                self.stack.pop()
                dfs()
            else:
                if List[index].isInteger():
                    return
                else:
                    self.stack[-1] = (List, index+1)
                    self.stack.append((List[index].getList(), 0))
                    dfs()
        
        dfs()
        return len(self.stack) > 0
                    
        
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

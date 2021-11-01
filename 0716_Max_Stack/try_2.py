from sortedcontainers import SortedDict

class Node:
    def __init__(self, value):
        self.value = value
        self.pre = None
        self.next = None

class MaxStack:

    def __init__(self):
        '''
        [why we choose hash structure]
        for popMax 
            => if we use list, the delete ops will be O(n)
            => but, if we use linked list, the delete ops will be O(n) (for search)
            => so, we have to use a 'hash' to store and get nodes => popMax (O(1) for search & delete)
        
        [why we choose treemap]
        for peekMax/popMax
            => we want a sorted hash structure to get the max element
            => hash-table is not suitable => it's hashed but not sorted
            => orderedDict is not suitable => it's hashed and ordered but not sorted
            => treemap is suitable => it's hashed and sorted
        
        for push/pop/top
            => we can maintain self.last to make it done => O(1)
        
        In the end, doubly linked list & treemap will speed up the time complexity to O(logn)
        '''
        self.head = Node(-float('inf')) # for popMax() (delete ops O(1))
        self.last = self.head           # for top()
        self.treemap = SortedDict()     # dict for store nodes to do operations (search O(logn)), get max (O(logn))

    def push(self, x: int) -> None:
        node = Node(x)
        
        # push node => O(1)
        self.last.next = node
        node.pre = self.last
        self.last = self.last.next
        
        # max-stack => O(logn)
        if x not in self.treemap:
            self.treemap[x] = []
        self.treemap[x].append(node)

    def pop(self) -> int:
        node = self.last
        
        # node => O(1)
        self.last = self.last.pre
        self.last.next = None
        node.pre = None
        
        # max-stack => O(logn)
        self.treemap[node.value].pop()
        if len(self.treemap[node.value]) == 0:
            del self.treemap[node.value]
        return node.value
        
    def top(self) -> int:
        # node => O(1)
        return self.last.value

    def peekMax(self) -> int:
        # max-stack => O(logn)
        return self.treemap.peekitem()[0] # peekitem() => get largest items pair (key, value)

    def popMax(self) -> int:
        # max-stack => O(logn)
        value, nodes = self.treemap.peekitem() # get node
        node = nodes[-1]
        
        self.treemap[value].pop()
        if len(self.treemap[value]) == 0:
            del self.treemap[value]
        
        # pop node => O(1)
        if node == self.last:
            self.last = self.last.pre
            self.last.next = None
            node.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.next = node.pre = None
        
        return value

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
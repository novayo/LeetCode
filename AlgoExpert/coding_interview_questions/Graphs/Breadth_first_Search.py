'''
main idea: BFS
time comp: O(V+E)
space comp: O(V)
- where V is the number of vertices of the input graph and E is the number of edges of the input graph
'''
import collections

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = collections.deque()
		queue.append(self)
		
		while queue:
			node = queue.popleft()
			array.append(node.name)
			for c in node.children:
				queue.append(c)
		return array

'''
main idea: dfs
time comp: O(V+E)
space comp: O(V)
- where V is the number of vertices of the input graph and E is the number of edges of the input graph
'''
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		
		def dfs(node):
			nonlocal array
			if not node:
				return
			
			array.append(node.name)
			for c in node.children:
				dfs(c)
		
		
		dfs(self)
        return array


'''
main idea: linkedlist
setHead: O(1) O(1)
setTail: O(1) O(1)
insertBefore: O(1) O(1)
insertAfter: O(1) O(1)
insertAtPosition: O(n) O(1)
removeNodesWithValue: O(n) O(1)
remove: O(1) O(1)
containsNodeWithValue: O(n) O(1)
'''
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if not self.head:
			self.head = node
			self.tail = node
		else:
			self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if not self.tail:
			self.head = node
			self.tail = node
		else:
			self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev == None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next == None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
			self.setHead(nodeToInsert)
		else:
			node = self.head
			p = 1
			while node and p != position:
				node = node.next
				p += 1
			if node:
				self.insertBefore(node, nodeToInsert)
			else:
				self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
		while node:
			removeNode = node
			node = node.next
			if removeNode.value == value:
				self.remove(removeNode)

    def remove(self, node):
        # Write your code here.
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev
		node.prev = None
		node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
		while node and node.value != value:
			node = node.next
		return node != None


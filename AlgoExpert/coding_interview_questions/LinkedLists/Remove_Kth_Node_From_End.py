'''
main idea: linkedlist
time comp: O(n)
space comp: O(1)
- where n is the number of the linked list
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    length = 0
	tmp = head
	while tmp:
		length += 1
		tmp = tmp.next
	
	tmp = head
	for _ in range(length-k-1):
		tmp = tmp.next
	
	if length == k:
		# because head is pass by reference, we can't do 'head = head.next'
		tmp = head
		while tmp.next.next:
			tmp.value = tmp.next.value
			tmp = tmp.next
		tmp.value = tmp.next.value
		tmp.next = None
	else:
		tmp.next = tmp.next.next


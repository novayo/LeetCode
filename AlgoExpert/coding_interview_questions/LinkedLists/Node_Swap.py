'''
main idea: swap first
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    # Write your code here.
	if not head or not head.next:
		return head
	
	# do first swap
	a = head
	b = head.next
	a.next = b.next
	b.next = a
	head = b
	
	# do rest swap
	while a.next and a.next.next:
		b = a.next
		c = a.next.next
		b.next = c.next
		c.next = b
		a.next = c
		a = b
	
    return head


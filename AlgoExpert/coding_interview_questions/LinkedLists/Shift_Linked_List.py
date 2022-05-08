'''
main idea: find length first
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    length = 0
	tmp = head
	while tmp:
		length += 1
		if not tmp.next:
			tmp.next = head
			break
		tmp = tmp.next
	
	k %= length
	tmp = head
	for _ in range(length-k-1):
		tmp = tmp.next
		
	head = tmp.next
	tmp.next = None
	return head

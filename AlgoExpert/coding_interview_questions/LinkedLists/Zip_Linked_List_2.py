'''
main idea: find middle and reverse and concate nodes I need
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    # Write your code here.
	middle = hare = linkedList
	while hare and hare.next and hare.next.next:
		middle = middle.next
		hare = hare.next.next
	
	middle.next = reverse(middle.next)
	tmp = middle.next
	middle.next = None
	middle = tmp
	
	ptr = linkedList
	while middle:
		tmp = middle.next
		middle.next = ptr.next
		ptr.next = middle
		middle = tmp
		ptr = ptr.next.next
	
    return linkedList

def print_all(head):
	tmp = head
	while tmp:
		print(tmp.value, end=' -> ')
		tmp = tmp.next
	print()

def reverse(head):
	if not head or not head.next:
		return head
	
	pre = head
	ptr = head.next
	
	while ptr:
		pre.next = ptr.next
		ptr.next = head
		head = ptr
		ptr = pre.next
	return head

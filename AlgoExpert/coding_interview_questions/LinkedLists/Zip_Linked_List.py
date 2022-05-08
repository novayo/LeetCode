'''
main idea: reverse
time comp: O(n^2)
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
	tmp = linkedList
	while tmp:
		tmp.next = reverse(tmp.next)
		tmp = tmp.next
    return linkedList

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

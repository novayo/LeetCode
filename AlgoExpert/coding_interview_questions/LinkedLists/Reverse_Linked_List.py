'''
main idea: swap to head
time comp: O(n)
space comp: O(1)
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    if not head or not head.next:
		return head
	
	pre = head
	ptr = head.next
	while ptr:
		pre.next = pre.next.next
		ptr.next = head
		head = ptr
		ptr = pre.next
	return head

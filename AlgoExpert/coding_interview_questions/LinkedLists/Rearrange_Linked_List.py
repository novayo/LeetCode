'''
main idea: find lower / equal / higher
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    # Write your code here.
    lptr = lower = LinkedList(-1)
	eptr = equal = LinkedList(-1)
	rptr = higher = LinkedList(-1)
	
	tmp = head
	while tmp:
		if tmp.value < k:
			lptr.next = tmp
			tmp = tmp.next
			lptr = lptr.next
			lptr.next = None
		elif tmp.value == k:
			eptr.next = tmp
			tmp = tmp.next
			eptr = eptr.next
			eptr.next = None
		else:
			rptr.next = tmp
			tmp = tmp.next
			rptr = rptr.next
			rptr.next = None
	
	head = ptr = lower
	for linkedlist in [lower, equal, higher]:
		ptr.next = linkedlist.next
		while ptr and ptr.next:
			ptr = ptr.next
	
	return head.next
	

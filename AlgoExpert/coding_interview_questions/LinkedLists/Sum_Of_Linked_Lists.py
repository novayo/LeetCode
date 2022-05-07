'''
main idea: linkedlist
space comp: O(n)
time comp: O(1)
- where n is the number of the input linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	l1 = linkedListOne
	l2 = linkedListTwo
	carry = 0
	pre = None
	while l1 or l2 or carry:
		cur_l1 = l1
		sum = carry
		if l1:
			sum += l1.value
			l1 = l1.next
		if l2:
			sum += l2.value
			l2 = l2.next
		
		if cur_l1:
			cur_l1.value = sum % 10
		else:
			cur_l1 = pre.next = LinkedList(sum % 10)
		carry = sum // 10
		pre = cur_l1
	
    return linkedListOne


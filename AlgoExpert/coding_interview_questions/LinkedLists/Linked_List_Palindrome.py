'''
main idea: find middle and reverse
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    # Write your code here.
	tortoise = hare = head
	while hare and hare.next and hare.next.next:
		tortoise = tortoise.next
		hare = hare.next.next
	
	tortoise.next = reverse(tortoise.next)
	tortoise = tortoise.next
	tmp = head
	while tortoise:
		if tmp.value != tortoise.value:
			return False
		tmp = tmp.next
		tortoise = tortoise.next
	
    return True

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

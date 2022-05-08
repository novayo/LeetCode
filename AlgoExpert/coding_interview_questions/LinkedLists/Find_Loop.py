'''
main idea: rare and tortoise
time comp: O(n)
space comp: O(1)
- where n is the number of nodes in linkedlist
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    rare = head.next.next
	tortoise = head.next
	while rare != tortoise:
		rare = rare.next.next
		tortoise = tortoise.next
	
	rare = head
	while rare != tortoise:
		rare = rare.next
		tortoise = tortoise.next
	return rare
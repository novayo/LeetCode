Question: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

---

try_1.py: O(nodes) O(nodes)
* Runtime: 52 ms, faster than 98.85% of Python3 online submissions for Populating Next Right Pointers in Each Node.
* Memory Usage: 15.3 MB, less than 75.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.

> bfs (lower level traversal)

---

try_2.py: O(nodes) O(1)
* Runtime: 60 ms, faster than 86.62% of Python3 online submissions for Populating Next Right Pointers in Each Node.
* Memory Usage: 15.3 MB, less than 60.71% of Python3 online submissions for Populating Next Right Pointers in Each Node.

> iteration every layers

---

try_3.py: O(nodes) O(1)
* Runtime: 52 ms, faster than 96.87% of Python3 online submissions for Populating Next Right Pointers in Each Node.
* Memory Usage: 16 MB, less than 16.51% of Python3 online submissions for Populating Next Right Pointers in Each Node.

> intuition
> 找出右邊，左邊next到右邊，左邊 = 右邊
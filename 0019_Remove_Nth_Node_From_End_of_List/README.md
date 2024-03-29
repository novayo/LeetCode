Question: https://leetcode.com/problems/search-in-rotated-sorted-array/

---

try_1.py: O(n)

* Runtime: 24 ms, faster than 96.71% of Python3 online submissions for Remove Nth Node From End of List.
* Memory Usage: 13.9 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

> one pass

---

try_2.py: O(n) O(1)

* Runtime: 32 ms, faster than 82.59% of Python3 online submissions for Remove Nth Node From End of List.
* Memory Usage: 14.2 MB, less than 76.81% of Python3 online submissions for Remove Nth Node From End of List.

> dummy node => one pass

---

try_3.py: O(n) O(1)

* Runtime: 26 ms, faster than 97.72% of Python3 online submissions for Remove Nth Node From End of List.
* Memory Usage: 13.9 MB, less than 59.74% of Python3 online submissions for Remove Nth Node From End of List.            

> linked list - dummy node

---

try_4.py: O(n) O(1)

* Runtime: 34 ms, faster than 72.31% of Python3 online submissions for Remove Nth Node From End of List.
* Memory Usage: 13.8 MB, less than 59.65% of Python3 online submissions for Remove Nth Node From End of List.

> linked list - two pass

---

try_5.ts: O(N) / O(1) - where N is the number of nodes in the list

* Runtime: 58 ms, faster than 59.24% of TypeScript online submissions for Remove Nth Node From End of List.
* Memory Usage: 44.5 MB, less than 65.92% of TypeScript online submissions for Remove Nth Node From End of List.

> linked list - one pass

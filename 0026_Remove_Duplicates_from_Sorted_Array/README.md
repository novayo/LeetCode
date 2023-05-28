Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

try_1.py:
* Runtime: 80 ms, faster than 90.18% of Python3 online submissions for Remove Duplicates from Sorted Array.
* Memory Usage: 15.7 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.

> intuition

---

try_2.py: O(n)
* Runtime: 76 ms, faster than 96.89% of Python3 online submissions for Remove Duplicates from Sorted Array.
* Memory Usage: 15.6 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.

> 遇到不相同的就交換到前面
	> 當遇到不同的，i+1，並交換i跟j

---

try_3.py: O(n) O(1)

* Runtime: 101 ms, faster than 44.03% of Python3 online submissions for Remove Duplicates from Sorted Array.
* Memory Usage: 18 MB, less than 31.49% of Python3 online submissions for Remove Duplicates from Sorted Array.

> in place

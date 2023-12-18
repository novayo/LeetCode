Question: https://leetcode.com/problems/add-and-search-word-data-structure-design/

---

try_1.py:
* Runtime: 404 ms, faster than 27.72% of Python3 online submissions for Add and Search Word - Data structure design.
* Memory Usage: 28.7 MB, less than 8.70% of Python3 online submissions for Add and Search Word - Data structure design.

> using trie

---

try_2.py:
* Runtime: 360 ms, faster than 51.78% of Python3 online submissions for Add and Search Word - Data structure design.
* Memory Usage: 28.6 MB, less than 8.70% of Python3 online submissions for Add and Search Word - Data structure design.

> optimize try_1.py

---

try_3.py: O(L + 26^2 + L) O(26^L) - where L is the length of the input string

* Runtime: 2598 ms, faster than 20.27% of Python3 online submissions for Design Add and Search Words Data Structure.
* Memory Usage: 82.8 MB, less than 10.33% of Python3 online submissions for Design Add and Search Words Data Structure. 

> Trie + recursion

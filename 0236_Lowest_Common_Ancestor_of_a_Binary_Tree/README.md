Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

---

try_1.py: O(n) O(n)
* Runtime: 2068 ms, faster than 5.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
* Memory Usage: 419.3 MB, less than 5.02% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

> 把p與q的path記起來為兩的list，之後去比較最後一個相同的

---

try_2.py: O(n) O(n)
* Runtime: 64 ms, faster than 92.97% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
* Memory Usage: 27.6 MB, less than 14.86% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

> 子樹有找到回傳True，左右都找到則為LCA
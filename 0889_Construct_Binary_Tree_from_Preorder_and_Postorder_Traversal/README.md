Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

---

try_1.py: O(n) O(n)

* Runtime: 56 ms, faster than 62.44% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
* Memory Usage: 14.4 MB, less than 38.67% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.

> 以兩邊為主，從preorder建立root，從postorder找left跟right

---

try_2.py: O(n) O(n)

* Runtime: 52 ms, faster than 78.83% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
* Memory Usage: 14.4 MB, less than 14.78% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.

> 以postorder去定義結束範圍

---

try_3.py: O(n) O(n)

* 以preorder為主

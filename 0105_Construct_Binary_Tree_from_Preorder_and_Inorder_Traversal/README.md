Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

---

try_1.py:

* Runtime: 156 ms, faster than 56.24% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
* Memory Usage: 52.4 MB, less than 39.47% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

> dfs to mimck inorder

---

try_2.py: O(n) O(n)

* Runtime: 56 ms, faster than 83.58% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
* Memory Usage: 18.9 MB, less than 63.16% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

> reduce the time of finding index

---

try_3.py: O(n) O(n)

* Runtime: 52 ms, faster than 96.70% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
* Memory Usage: 18.8 MB, less than 82.55% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

> 先看preorder建立root，此點在inorder內的左邊為左子樹，右邊為右子樹
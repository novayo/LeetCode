Question: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

---

try_1.py: O(n) O(n)
* Runtime: 168 ms, faster than 33.22% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 53.1 MB, less than 32.15% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> 以postorder為基準，從右找到左邊去對應inorder

---

try_2.py: O(n) O(n)
* Runtime: 52 ms, faster than 90.52% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 19.1 MB, less than 52.19% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> try_1.py的改良，減少找尋index的時間

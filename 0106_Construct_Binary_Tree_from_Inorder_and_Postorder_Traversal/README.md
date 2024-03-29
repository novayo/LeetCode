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

---

try_3.py: O(n) O(n)

* Runtime: 56 ms, faster than 89.90% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 19.1 MB, less than 64.10% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> inorder反過來，從尾巴開始看，先處理右邊在處理左邊

---

try_4.py: O(n) O(n)

* Runtime: 52 ms, faster than 94.69% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 19 MB, less than 76.00% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> 從inorder定義結束範圍
        
---

try_5.py: O(n) O(n)

* Runtime: 87 ms, faster than 62.76% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 19.2 MB, less than 65.53% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> 以postorder為主

---

try_6.py: O(n) O(n)

* Runtime: 60 ms, faster than 93.59% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
* Memory Usage: 19 MB, less than 61.66% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

> recursion
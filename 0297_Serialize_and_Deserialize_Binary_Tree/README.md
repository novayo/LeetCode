Question: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

---

try_1.py: O(n) O(n)
* Runtime: 92 ms, faster than 98.86% of Python3 online submissions for Serialize and Deserialize Binary Tree.
* Memory Usage: 19.3 MB, less than 21.95% of Python3 online submissions for Serialize and Deserialize Binary Tree.

> bfs
> 用list為主軸，index從1開始，i是左邊，i+1是右邊，把非null的給加進去queue即可
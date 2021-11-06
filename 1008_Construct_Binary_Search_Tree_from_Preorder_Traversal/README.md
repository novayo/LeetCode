Question: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

---

try_1.py: O(n) O(n)
* Runtime: 24 ms, faster than 99.66% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
* Memory Usage: 13.6 MB, less than 6.67% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.

> stack
	> if next val is greater than this val, pop the stack until stack[-1] > next val and set the last pop item .right to next val and finally append into stack
	> else stack[-1].left = next val and append(stack[-1].left)

---

try_2.py: O(n) O(n)

* Runtime: 36 ms, faster than 87.87% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
* Memory Usage: 14.5 MB, less than 14.74% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.

> 以root去找第一個較大值的位置，定義left, right範圍
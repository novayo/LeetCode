Question: https://leetcode.com/problems/permutations/

---

try_1.py:
* Runtime: 44 ms, faster than 22.55% of Python3 online submissions for Permutations.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations.

> next permutation

---

try_2.py:
* Runtime: 32 ms, faster than 95.41% of Python3 online submissions for Permutations.
* Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations.

> itertools.permutations

---

try_3.py:
* Runtime: 36 ms, faster than 85.78% of Python3 online submissions for Permutations.
* Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Permutations.

> backtracking
> 第i個與後面j個交換，交換後再recr(i+1)，之看這個組合的下一個交換

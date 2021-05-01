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

---

try_4.py:
* Runtime: 40 ms, faster than 64.51% of Python3 online submissions for Permutations.
* Memory Usage: 14.6 MB, less than 14.67% of Python3 online submissions for Permutations.

> backtracking
> 單純找尋所有組合

---

try_5.py:
* Runtime: 28 ms, faster than 99.27% of Python3 online submissions for Permutations.
* Memory Usage: 14.5 MB, less than 43.18% of Python3 online submissions for Permutations.

> 每個index都去跟後面的index交換即可

---

try_6.py:
* Runtime: 40 ms, faster than 64.51% of Python3 online submissions for Permutations.
* Memory Usage: 14.2 MB, less than 97.01% of Python3 online submissions for Permutations.

> next_permutation

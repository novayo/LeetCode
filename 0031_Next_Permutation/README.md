Question: https://leetcode.com/problems/next-permutation/

---

try_1.py:
* Runtime: 28 ms, faster than 99.54% of Python3 online submissions for Next Permutation.
* Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Next Permutation.

> Follow by "https://imgur.com/UVLEPWG"

---

try_2.py: O(n) O(1)

* Runtime: 44 ms, faster than 52.12% of Python3 online submissions for Next Permutation.
* Memory Usage: 14.2 MB, less than 80.42% of Python3 online submissions for Next Permutation.

> # 往左找第一個小的 => a
> # 往右找下一個 略大於a的 => b
> # 交換a, b
> # reverse a+1~b-1

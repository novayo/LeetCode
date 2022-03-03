Question: https://leetcode.com/problems/contiguous-array/

---

try_1.py:
* Runtime: 912 ms, faster than 63.72% of Python3 online submissions for Contiguous Array.
* Memory Usage: 18.3 MB, less than 16.67% of Python3 online submissions for Contiguous Array.

> dp

---

try_2.py: O(n) O(n)

* Runtime: 872 ms, faster than 91.18% of Python3 online submissions for Contiguous Array.
* Memory Usage: 19.5 MB, less than 41.43% of Python3 online submissions for Contiguous Array.

> 遇到1的時候+1，0的時候-1
> [....3........3.....]
> 第一個3表示: 從0開始往後計算
> 第二個3表示: 從0開始往後計算
> 此時第一個3~第二個3之前就是 答案
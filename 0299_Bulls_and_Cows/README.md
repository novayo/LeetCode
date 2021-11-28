Question: https://leetcode.com/problems/bulls-and-cows/
---

try_1.py: O(n)

* Runtime: 40 ms, faster than 87.53% of Python3 online submissions for Bulls and Cows.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.

> straightforward

---

try_2.py: O(n)

* Runtime: 28 ms, faster than 99.63% of Python3 online submissions for Bulls and Cows.
* Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.

> straightforward

---

try_3.py: O(n)

* Runtime: 57 ms, faster than 26.20% of Python3 online submissions for Bulls and Cows.
* Memory Usage: 14.2 MB, less than 84.09% of Python3 online submissions for Bulls and Cows.

> 掃過一遍secret、guess後取得幾A，跟其他個數
> union keys => 並指loop keys求最小 => 幾B累加
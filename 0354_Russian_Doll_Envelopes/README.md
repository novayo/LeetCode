Question: https://leetcode.com/problems/russian-doll-envelopes/

---

try_1.py: O(n^2) O(n)

* TLE

> DP
> 排序後從尾巴找尋有幾個比自己大，取最大者的值+1(自己本身)

---

try_2.py: O(nlogn) O(n)

* Runtime: 164 ms, faster than 54.13% of Python3 online submissions for Russian Doll Envelopes.
* Memory Usage: 16.5 MB, less than 57.87% of Python3 online submissions for Russian Doll Envelopes.

> patient sort
> 排序過後，就跟300題一樣，因此也可以轉換成接龍遊戲，使用patient sort

---

try_3.py: O(nlogn) O(n)

* Runtime: 1852 ms, faster than 42.93% of Python3 online submissions for Russian Doll Envelopes.
* Memory Usage: 61.7 MB, less than 60.78% of Python3 online submissions for Russian Doll Envelopes.

> patient sort

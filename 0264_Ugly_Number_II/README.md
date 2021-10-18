Question: https://leetcode.com/problems/ugly-number-ii/

---

try_1.py: O(n) O(n)

* Runtime: 156 ms, faster than 62.41% of Python3 online submissions for Ugly Number II.
* Memory Usage: 14.3 MB, less than 48.90% of Python3 online submissions for Ugly Number II.

> 用2 3 5由小到大產生乘積

---
try_2.py: O(n) O(n)

* Runtime: 195 ms, faster than 48.41% of Python3 online submissions for Ugly Number II.
* Memory Usage: 14.4 MB, less than 21.03% of Python3 online submissions for Ugly Number II.

> 拿之前的紀錄，*2 *3 *5看哪個小，就填入那個值，之後該index要+1(之後再去比較下一個*2 *3 *5)，所以必須把過程給記錄下來
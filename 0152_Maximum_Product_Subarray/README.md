Question: https://leetcode.com/problems/maximum-product-subarray/

---

try_1.py: O(n) O(1)

* Runtime: 88 ms, faster than 20.92% of Python3 online submissions for Maximum Product Subarray.
* Memory Usage: 14.3 MB, less than 84.95% of Python3 online submissions for Maximum Product Subarray.

> 依照0去做分割，計算每個區塊的最大乘積，最大乘積= max(全部相乘, 全部相乘/左邊第一個負之前的總product, 全部相乘/右邊第一個負之後的總product)
> 看去除最左邊還是最右邊會最大

---

try_2.py: O(n) O(1)

* Runtime: 72 ms, faster than 35.95% of Python3 online submissions for Maximum Product Subarray.
* Memory Usage: 14.4 MB, less than 36.70% of Python3 online submissions for Maximum Product Subarray.

> 單純掃過所有可能，從左邊掃，從右邊掃，紀錄當前最大的sub即可
> 若乘完後=0，則再從1開始乘

---

try_3.py: O(n) O(1)

* Runtime: 88 ms, faster than 47.73% of Python3 online submissions for Maximum Product Subarray.
* Memory Usage: 14.4 MB, less than 87.07% of Python3 online submissions for Maximum Product Subarray.

> 紀錄cur max & cur min

---

try_4.py: O(n) O(1)

* Runtime: 92 ms, faster than 82.20% of Python3 online submissions for Maximum Product Subarray.
* Memory Usage: 14.4 MB, less than 84.45% of Python3 online submissions for Maximum Product Subarray.

> 紀錄cur max & cur min

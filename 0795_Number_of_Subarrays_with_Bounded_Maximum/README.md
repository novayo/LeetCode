Question: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

---

try_1.py: O(n) O(1)

* Runtime: 428 ms, faster than 19.55% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
* Memory Usage: 19.8 MB, less than 5.13% of Python3 online submissions for Number of Subarrays with Bounded Maximum.

> 若都無超過right，則可以加入計算 => 若符合條件 => 加 從上一個大的到目前的index距離、若不符合，則繼續上一個嘗試
> 若超過right => 更新最大位置，嘗試歸零

---

try_2.py: O(n) O(1)

* Runtime: 570 ms, faster than 90.30% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
* Memory Usage: 22.2 MB, less than 68.41% of Python3 online submissions for Number of Subarrays with Bounded Maximum.

> analysis
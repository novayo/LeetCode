Question: https://leetcode.com/problems/car-fleet-ii/

---

try_1.py: O(n^2) O(n)

* 85 / 85 test cases passed, but took too long.

> 更新hit time，並且去更新所有可能(此點的前後會不會互撞，會的話要更新時間)

---

try_2.py: O(nlogn) O(n)

* Runtime: 3052 ms, faster than 6.11% of Python3 online submissions for Car Fleet II.
* Memory Usage: 76.2 MB, less than 5.22% of Python3 online submissions for Car Fleet II.

> 用prioirty queue
> 從小到大更新hit time，並且去更新所有可能(此點的前後會不會互撞，會的話要更新時間)

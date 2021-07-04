Question: https://leetcode.com/problems/car-fleet/

---

try_1.py: O(nlogn) O(n)

* Runtime: 160 ms, faster than 93.09% of Python3 online submissions for Car Fleet.
* Memory Usage: 16.7 MB, less than 79.77% of Python3 online submissions for Car Fleet.

> 用距離排序(因為不能超車)，計算每個人的到達時間點
> 後面的人到達的時間點
> 	如果小於等於前面的人 => 會疊在一起
> 	如果大於前面的人 => 則可以算一台

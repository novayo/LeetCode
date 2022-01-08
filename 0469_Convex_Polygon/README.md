Question: https://leetcode.com/problems/convex-polygon/

---

try_1.py: O(n) O(1)

* Runtime: 321 ms, faster than 9.38% of Python3 online submissions for Convex Polygon.
* Memory Usage: 19.4 MB, less than 21.88% of Python3 online submissions for Convex Polygon.

> 計算所有  180-夾角(假設所有角度為內角) => 若加起來==360 => True
> 若計算過程中>360 => return False

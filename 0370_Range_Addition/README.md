Question: https://leetcode.com/problems/range-addition/

---

try_1.py: O(n) O(1)

* Runtime: 168 ms, faster than 82.55% of Python3 online submissions for Range Addition.
* Memory Usage: 22.7 MB, less than 77.85% of Python3 online submissions for Range Addition.

> 轉成累加形式，所以開頭要相加，結尾+1要扣除(累加前面時才不會多算)

---

try_2.py: O(n) O(1)

* Runtime: 234 ms, faster than 52.75% of Python3 online submissions for Range Addition.
* Memory Usage: 22.8 MB, less than 20.35% of Python3 online submissions for Range Addition.

> sweep line

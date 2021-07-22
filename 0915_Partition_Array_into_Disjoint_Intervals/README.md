Question: https://leetcode.com/problems/partition-array-into-disjoint-intervals/

---

try_1.py: O(nlogn) O(n)

* Runtime: 2860 ms, faster than 5.06% of Python3 online submissions for Partition Array into Disjoint Intervals.
* Memory Usage: 18.5 MB, less than 31.18% of Python3 online submissions for Partition Array into Disjoint Intervals.

> left max must > right min 

---

try_2.py: O(n) O(n)

* Runtime: 224 ms, faster than 31.04% of Python3 online submissions for Partition Array into Disjoint Intervals.
* Memory Usage: 18.6 MB, less than 8.57% of Python3 online submissions for Partition Array into Disjoint Intervals.

> left max must > right min

---

try_3.py: O(n) O(1)

* Runtime: 176 ms, faster than 92.42% of Python3 online submissions for Partition Array into Disjoint Intervals.
* Memory Usage: 18.4 MB, less than 31.18% of Python3 online submissions for Partition Array into Disjoint Intervals.

> 遇到更小值的再更新目前最大值即可


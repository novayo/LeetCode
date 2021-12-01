Question: https://leetcode.com/problems/meeting-rooms-ii/

---

try_1.py: O(nlogn) O(n)

* Runtime: 80 ms, faster than 54.72% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.6 MB, less than 6.15% of Python3 online submissions for Meeting Rooms II.

> 去紀錄有幾個房間要被使用，用完的就pop（有新時間>end時間）

---

try_2.py: O(nlogn) O(n)

* Runtime: 87 ms, faster than 48.23% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.5 MB, less than 65.27% of Python3 online submissions for Meeting Rooms II.

> 去紀錄有幾個房間要被使用，用完的就pop（有新時間>end時間）

---

try_3.py: O(nlogn) O(n)

* Runtime: 80 ms, faster than 59.12% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.5 MB, less than 66.52% of Python3 online submissions for Meeting Rooms II.

> sweep line

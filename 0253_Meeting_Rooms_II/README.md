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

---

try_4.py: O(nlogn) O(n)

* Runtime: 144 ms, faster than 27.39% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.5 MB, less than 49.16% of Python3 online submissions for Meeting Rooms II.

> heap

---

try_5.py: O(nlogn) O(n)

* Runtime: 153 ms, faster than 20.70% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.4 MB, less than 83.76% of Python3 online submissions for Meeting Rooms II.

> heap

---

try_6.py: O(n) O(n)

* Runtime 9835 ms Beats 5.12%
* Memory 27.3 MB Beats 5.12%

> sweep line

---

try_7.py: O(nlogn) O(n)

* Runtime 105 ms Beats 16.20%
* Memory 20.9 MB Beats 7.12%

> hashmap + sort + sweep line

---

try_8.py: O(nlogn) O(n)

* Runtime 99 ms Beats 42.68%
* Memory 19.9 MB Beats 74.48%

> heap
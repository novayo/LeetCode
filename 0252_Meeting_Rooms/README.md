Question: https://leetcode.com/problems/meeting-rooms/

---

try_1.py: O(n)
* Runtime: 76 ms, faster than 82.12% of Python3 online submissions for Meeting Rooms. 
* Memory Usage: 17.1 MB, less than 28.91% of Python3 online submissions for Meeting Rooms.

> [[0,5],[4,6],[6,7],[7,10]]
> 排序過後，
> 去看是否 [0,5],[4,6] => 下一個的左邊(4) 是否大於 上一個的右邊(5)

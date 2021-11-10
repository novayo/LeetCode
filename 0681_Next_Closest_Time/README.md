Question: https://leetcode.com/problems/next-closest-time/

---

try_1.py: O(4^4) O(4^4)

* Runtime: 36 ms, faster than 48.73% of Python3 online submissions for Next Closest Time.
* Memory Usage: 14.3 MB, less than 34.32% of Python3 online submissions for Next Closest Time.

> find out all possibility and filter less and greater one
> if there's something in greater => the answer must be min(greater)
> elif there's something in less  => the answer must be min(less) as well
> else => the answer must be "time" and time is like 11:11 / 22:22

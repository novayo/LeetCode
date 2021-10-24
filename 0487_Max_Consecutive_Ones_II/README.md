Question: https://leetcode.com/problems/max-consecutive-ones-ii/

---

try_1.py: O(n) O(n)
* Runtime: 372 ms, faster than 94.55% of Python3 online submissions for Max Consecutive Ones II.
* Memory Usage: 13.8 MB, less than 98.26% of Python3 online submissions for Max Consecutive Ones II.

> two pass

---

try_2.py: O(n) O(1)
* Runtime: 444 ms, faster than 53.33% of Python3 online submissions for Max Consecutive Ones II.
* Memory Usage: 14.2 MB, less than 19.74% of Python3 online submissions for Max Consecutive Ones II.

> one pass

---

try_3.py: O(n) O(n)

* Runtime: 428 ms, faster than 47.95% of Python3 online submissions for Max Consecutive Ones II.
* Memory Usage: 15 MB, less than 5.14% of Python3 online submissions for Max Consecutive Ones II.

> 紀錄此index下，左邊有幾個1(prefix)，右邊有幾個1(suffix)，之再loop一次去計算max即可
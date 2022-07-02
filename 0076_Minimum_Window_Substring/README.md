Question: https://leetcode.com/problems/minimum-window-substring/

---

try_1.py: O(MN)
* Runtime: 348 ms, faster than 18.10% of Python3 online submissions for Minimum Window Substring.
* Memory Usage: 14.3 MB, less than 5.55% of Python3 online submissions for Minimum Window Substring.

> intuition
	> 用兩個pointer去跑，並記錄個數，如果所在位置的累積的文字個數>=要求的問字個數的話，就減掉，並把左pointer移到下一個要求的文字的index

---

try_2.py: O(52n) O(52)

* Runtime: 923 ms, faster than 5.01% of Python3 online submissions for Minimum Window Substring.
* Memory Usage: 14.8 MB, less than 35.83% of Python3 online submissions for Minimum Window Substring.

> two pointer

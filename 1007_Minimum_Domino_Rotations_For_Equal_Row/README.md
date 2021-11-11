Question: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

---

try_1.py: O(n^2)
* Runtime: 1280 ms, faster than 32.88% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
* Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

> intuition, greedy

---

try_2.py: O(n)
* Runtime: 1192 ms, faster than 78.54% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
* Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

> greedy
	> 因為如果要是2的話，那不管是哪個組合，一定上下只少有一個2，因此只要選擇任一一組，去往後跑一次確認是否其他組合都有至少一個2就可以了
	> 所以，我們可以選擇index=0，那答案也在(A[0], B[0])的組合中，去loop一次即可

---

try_3.py: O(n) O(n)

* Runtime: 1336 ms, faster than 28.70% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
* Memory Usage: 19.5 MB, less than 7.06% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

> intuition

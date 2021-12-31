Question: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

---

try_1.py: O(n) O(n)

* Runtime: 48 ms, faster than 91.09% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.
* Memory Usage: 16.7 MB, less than 23.27% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.

> dfs
> 對每個node來說，區分遞增遞減的數值(有可能都是遞減)
> 每個點區計算一次左右值的可能性並紀錄當前最大

---

try_2.py: O(n) O(n)

* Runtime: 52 ms, faster than 72.04% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.
* Memory Usage: 16.5 MB, less than 48.75% of Python3 online submissions for Binary Tree Longest Consecutive Sequence II.

> dfs => return cur_inc, cur_dec

Question: https://leetcode.com/problems/number-of-boomerangs/

---

try1.py: O(n^2) O(n)

* Runtime: 1100 ms, faster than 82.21% of Python3 online submissions for Number of Boomerangs.
* Memory Usage: 27.3 MB, less than 25.07% of Python3 online submissions for Number of Boomerangs.

> 固定第一個，剩下的Cn取1，Cn-1取1 => 故只要紀錄個數，取出個數>=2的（可組成3個），就可以計算答案
> 因為點都不重複，不需考慮 dist=0的問題

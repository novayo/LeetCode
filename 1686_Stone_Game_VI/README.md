Question: https://leetcode.com/problems/stone-game-vi/

---

try_1.py: O(nlogn) O(n)
* Runtime: 1360 ms, faster than 44.94% of Python3 online submissions for Stone Game VI.
* Memory Usage: 28.5 MB, less than 47.78% of Python3 online submissions for Stone Game VI.

> Alice: 如果B[i]很大，則選擇A[i]（因為不讓B[i]選擇）
> Bob: 如果B[i]很大，則選擇B[i]（因為B要選大的）
> 反之亦然 A[i]很大的話
> 所以每次選擇A[i]+B[i]的最大值即可

---

try_2.py: O(nlogn) O(n)

* Runtime: 1723 ms, faster than 55.00% of Python3 online submissions for Stone Game VI.
* Memory Usage: 28.9 MB, less than 35.00% of Python3 online submissions for Stone Game VI.

> 大的就先選，一方面讓自己最大，一方面讓別人最小
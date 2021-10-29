Question: https://leetcode.com/problems/maximum-length-of-pair-chain/

---

try_1.py: O(nlogn) O(n)

* Runtime: 824 ms, faster than 44.46% of Python3 online submissions for Maximum Length of Pair Chain.
* Memory Usage: 15.1 MB, less than 9.77% of Python3 online submissions for Maximum Length of Pair Chain.

> use dp to store previous answer
> in any index => we want to looking for the max answer from 0~index-1 and satisfying the condition => we can use heap to handle it

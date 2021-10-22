Question: https://leetcode.com/problems/paint-house-ii/

---

try_1.py: O(nk) O(1)

* Runtime: 96 ms, faster than 98.05% of Python3 online submissions for Paint House II.
* Memory Usage: 14.4 MB, less than 35.81% of Python3 online submissions for Paint House II.

> 往前找最小 & index不相等的值相加即可
> 最小其實只有兩個 [5,3,2,1,5] => 最小就是1 2 => 故要這樣加 => [5+1,3+1,2+1,1+2,5+1] => 只有最小的要加第二小的
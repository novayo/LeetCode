Question: https://leetcode.com/problems/arithmetic-slices/

---

try_1.py: O(n) O(1)

* Runtime: 72 ms, faster than 9.19% of Python3 online submissions for Arithmetic Slices.
* Memory Usage: 14.5 MB, less than 45.55% of Python3 online submissions for Arithmetic Slices.

> [1,2,3] => 1個, [1,2,3,4] => 1+2個, [1,2,3,4,5] => 1+2+3個...以此類推
> 所以只需要去找尋總共有多少個連續的就能夠計算答案
> [1,2,3,4,5,8,11]  而找完前五個後，再來要從剛剛找的最後一位(5)繼續往後找即可 => 所以時間複雜度為O(n)
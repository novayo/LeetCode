Question: https://leetcode.com/problems/single-number-iii/

---

try_1.py: O(n) O(1)

* Runtime: 143 ms, faster than 15.65% of Python3 online submissions for Single Number III.
* Memory Usage: 15.8 MB, less than 67.16% of Python3 online submissions for Single Number III.

> after xor => a2 is represented as xor of two number
> find any 1 in bin(number) to represent one of answer
> a1 = loop nums again to perform xor if num & bin(number) == 0
> return a1, a2^a1

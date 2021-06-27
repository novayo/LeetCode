Question: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

---

try_1.py: O(n^2) O(n)

* Runtime: 32 ms, faster than 51.76% of Python3 online submissions for Numbers At Most N Given Digit Set.
* Memory Usage: 14.4 MB, less than 7.06% of Python3 online submissions for Numbers At Most N Given Digit Set.

> 1. calculate number of less than n digits => combination problem
> 2. calculate number of n digit => recursion to calculate possible number

---

try_2.py: O(nlogn) O(n)

* Runtime: 28 ms, faster than 80.00% of Python3 online submissions for Numbers At Most N Given Digit Set.
* Memory Usage: 14.2 MB, less than 81.18% of Python3 online submissions for Numbers At Most N Given Digit Set.

> 1. calculate number of less than n digits => combination problem
> *2. calculate number of n digit => recursion to calculate possible number
>   => *2. use binary search

---

try_3.py: O(nlogn) O(n)

* Runtime: 28 ms, faster than 81.61% of Python3 online submissions for Numbers At Most N Given Digit Set.
* Memory Usage: 14.3 MB, less than 60.92% of Python3 online submissions for Numbers At Most N Given Digit Set.

> refine try_2.py
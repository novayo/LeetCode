Question: https://leetcode.com/problems/integer-break/

---

try_1.py: O(n^2) O(n)

* Runtime: 32 ms, faster than 79.85% of Python3 online submissions for Integer Break.
* Memory Usage: 14.3 MB, less than 48.63% of Python3 online submissions for Integer Break.

> like coin change to store max pre answer and reuse it
> https://leetcode.com/problems/integer-break/discuss/383679/Python-DP-solution-with-detailed-explanation.-Avoids-confusion-about-factors-of-2-or-3.

---

try_2.py: O(n) O(1)

* Runtime: 32 ms, faster than 90.25% of Python3 online submissions for Integer Break.
* Memory Usage: 13.8 MB, less than 88.39% of Python3 online submissions for Integer Break.

> 當n>4時，則盡量給3
> 因為 3*3 > 2*2*2

---

try_3.py: O(n) O(n)

* Runtime: 56 ms, faster than 30.08% of Python3 online submissions for Integer Break.
* Memory Usage: 13.9 MB, less than 88.39% of Python3 online submissions for Integer Break.

> 嘗試所有可能
Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
---

try_1.py: O(n)

* Runtime: 128 ms, faster than 7.93% of Python3 online submissions for Evaluate Reverse Polish Notation.
* Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Evaluate Reverse Polish Notation.

> stack from the back of tokens

---

try_2.py: O(n)

* Runtime: 116 ms, faster than 10.19% of Python3 online submissions for Evaluate Reverse Polish Notation.
* Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Evaluate Reverse Polish Notation.

> stack from the beginning of tokens
> storing str in stack and using eval to compute

---

try_3.py: O(n)

* Runtime: 68 ms, faster than 90.67% of Python3 online submissions for Evaluate Reverse Polish Notation.
* Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Evaluate Reverse Polish Notation.

> stack from the beginning of tokens
> storing int in stack and computing directly when pop from stack

---

try_4.py: O(n)

* Runtime: 120 ms, faster than 9.12% of Python3 online submissions for Evaluate Reverse Polish Notation.
* Memory Usage: 14.6 MB, less than 72.69% of Python3 online submissions for Evaluate Reverse Polish Notation.

> stack

---

try_5.py: O(n) O(n)

* Runtime: 135 ms, faster than 20.10% of Python3 online submissions for Evaluate Reverse Polish Notation.
* Memory Usage: 14.4 MB, less than 56.91% of Python3 online submissions for Evaluate Reverse Polish Notation.

> stack

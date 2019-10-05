Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
---

try_1.py: O(n) 140ms
> stack from the back of tokens

try_2.py: O(n) 132ms
> stack from the beginning of tokens
> storing str in stack and using eval to compute

try_3.py: O(n) 100ms
> stack from the beginning of tokens
> storing int in stack and computing directly when pop from stack

Question: https://leetcode.com/problems/implement-queue-using-stacks/

---

try_1.py: O(n) O(n)
* Runtime: 28 ms, faster than 76.75% of Python3 online submissions for Implement Queue using Stacks.
* Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.

> 每次push都排序一次
> push: O(n)
> pop: O(1)
> peek: O(1)
> empty: O(1)

---

try_2.py: O(n)  O(n)
* Runtime: 24 ms, faster than 92.71% of Python3 online submissions for Implement Queue using Stacks.
* Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.

> 只有在要pop或peek時才排序
> push: O(1)
> pop: amortized O(1), O(n)
> peek: amortized O(1), O(n)
> empty: O(1)

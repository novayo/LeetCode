Question: https://leetcode.com/problems/palindrome-partitioning-ii/

---

try_1.py: O(n^3) O(n)
* Runtime: 96 ms, faster than 92.68% of Python3 online submissions for Palindrome Partitioning II.
* Memory Usage: 14.3 MB, less than 70.96% of Python3 online submissions for Palindrome Partitioning II.

> dp

---

try_2.py: O(n^2) O(n)

* Runtime: 452 ms, faster than 81.93% of Python3 online submissions for Palindrome Partitioning II.
* Memory Usage: 37.9 MB, less than 48.73% of Python3 online submissions for Palindrome Partitioning II.

> dp
> First of all, find out all palindrome and store in dp ({index: [can go to which index]})
> Next, use recursion + dp to find out less steps through dp
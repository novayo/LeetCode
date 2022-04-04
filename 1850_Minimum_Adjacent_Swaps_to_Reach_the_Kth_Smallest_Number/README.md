Question: https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

---

try_1.py: O(k*ans*len(s)) O(ans*len(s))

* TLE

> next permutation + bfs

---

try_2.py: O(k*n^2) O(n)

* Runtime: 2139 ms, faster than 57.03% of Python3 online submissions for Minimum Adjacent Swaps to Reach the Kth Smallest Number.
* Memory Usage: 13.9 MB, less than 95.87% of Python3 online submissions for Minimum Adjacent Swaps to Reach the Kth Smallest Number.

> next permutation + compare

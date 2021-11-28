Question: https://leetcode.com/problems/sentence-similarity-ii/

---

try_1.py: O(n) O(n)

* Runtime: 488 ms, faster than 55.66% of Python3 online submissions for Sentence Similarity II.
* Memory Usage: 15.7 MB, less than 86.56% of Python3 online submissions for Sentence Similarity II.

> disjoint set to merge two string
> if the same means their parents are the same (Same as LC947)

---

try_2.py: O(n^2) O(n)

* Runtime: 814 ms, faster than 9.05% of Python3 online submissions for Sentence Similarity II.
* Memory Usage: 16.8 MB, less than 8.83% of Python3 online submissions for Sentence Similarity II.

> build graph and find parent by dfs
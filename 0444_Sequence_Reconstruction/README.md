Question: https://leetcode.com/problems/sequence-reconstruction/

---

try_1.py: O(n) O(n)

* Runtime: 484 ms, faster than 42.60% of Python3 online submissions for Sequence Reconstruction.
* Memory Usage: 20.1 MB, less than 21.45% of Python3 online submissions for Sequence Reconstruction.

> topological to check if there's only one possibility in any step.
> also check if all values in org are in seqs, in contrast, all values in seqs are in org
> check if ans == org

Question: https://leetcode.com/problems/delete-nodes-and-return-forest/

---

try_1.py: O(n) O(n)

* Runtime: 60 ms, faster than 95.46% of Python3 online submissions for Delete Nodes And Return Forest.
* Memory Usage: 15.2 MB, less than 27.53% of Python3 online submissions for Delete Nodes And Return Forest.

> dfs => when bottom-up 
> => if deleted, append left & right in list
> => else, create node and join left & right

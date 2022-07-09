Question: https://leetcode.com/problems/delete-nodes-and-return-forest/

---

try_1.py: O(n) O(n)

* Runtime: 60 ms, faster than 95.46% of Python3 online submissions for Delete Nodes And Return Forest.
* Memory Usage: 15.2 MB, less than 27.53% of Python3 online submissions for Delete Nodes And Return Forest.

> dfs => when bottom-up 
> => if deleted, append left & right in list
> => else, create node and join left & right

---

try_2.py: O(n) O(n)

* Runtime: 64 ms, faster than 86.36% of Python3 online submissions for Delete Nodes And Return Forest.
* Memory Usage: 15 MB, less than 26.60% of Python3 online submissions for Delete Nodes And Return Forest.

> dfs

---

try_3.py: O(n) O(w+d) - n is the number of nodes of the input tree and w is the width and d is the depth.

* Runtime: 72 ms, faster than 89.02% of Python3 online submissions for Delete Nodes And Return Forest.
* Memory Usage: 14.5 MB, less than 71.41% of Python3 online submissions for Delete Nodes And Return Forest.

> dfs

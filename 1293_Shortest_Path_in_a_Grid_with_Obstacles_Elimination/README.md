Question: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

---

try_1.py: O(n) O(n)

* Runtime: 120 ms, faster than 59.41% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
* Memory Usage: 14.4 MB, less than 96.15% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.

> bfs 跑所有可能 => 每層代表的意思是 目前可以走的node
> 要記錄已走過的值，走道重複的 且 此時的k比之前走過的小 => 就不用走這個組合了
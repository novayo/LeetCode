Question: https://leetcode.com/problems/01-matrix/

---

try_1.py: O(n) O(n)
* Runtime: 696 ms, faster than 65.80% of Python3 online submissions for 01 Matrix.
* Memory Usage: 17.5 MB, less than 12.50% of Python3 online submissions for 01 Matrix.

> bfs
> 用0去找最近的1

---

try_2.py: O(n) O(n)
* Runtime: 464 ms, faster than 99.84% of Python3 online submissions for 01 Matrix.
* Memory Usage: 16.4 MB, less than 12.50% of Python3 online submissions for 01 Matrix.

> bfs
> 找1，若1的上下左右都大於等於自己(代表周圍沒有0)，則自己加一，再丟回去queue內

---

try_3.py: O(n) O(n)

* Runtime: 708 ms, faster than 59.46% of Python3 online submissions for 01 Matrix.
* Memory Usage: 18.1 MB, less than 14.77% of Python3 online submissions for 01 Matrix.

> 將0n算成起始點，往後加入上下左右，計算層數即可

---

try_4.py: O(n) O(n)

* Runtime: 720 ms, faster than 57.42% of Python3 online submissions for 01 Matrix.
* Memory Usage: 18.3 MB, less than 6.86% of Python3 online submissions for 01 Matrix.

> 將0n算成起始點，往後加入上下左右，計算層數即可

Question: https://leetcode.com/problems/design-tic-tac-toe/

---

try_1.py: O(1)
* Runtime: 88 ms, faster than 90.03% of Python3 online submissions for Design Tic-Tac-Toe.
* Memory Usage: 16.5 MB, less than 16.26% of Python3 online submissions for Design Tic-Tac-Toe.

> 一個move近來後，直接分別紀錄他的row, col, 跟斜對角
> 如果有n個就表示贏了，輸出player

---

try_2.py: O(1) O(4n)

* Runtime: 88 ms, faster than 80.59% of Python3 online submissions for Design Tic-Tac-Toe.
* Memory Usage: 16.9 MB, less than 31.19% of Python3 online submissions for Design Tic-Tac-Toe.

> check four direction

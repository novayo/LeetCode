Question: https://leetcode.com/problems/perfect-squares/

---

try_1.py: O(n*sqrt(n)) O(n)
* Runtime: 4280 ms, faster than 48.07% of Python3 online submissions for Perfect Squares.
* Memory Usage: 14.2 MB, less than 5.00% of Python3 online submissions for Perfect Squares.

> dp
> 去紀錄從自己開始往前的幾個平方數中的最小值去+1即可 (從自己往前推減掉某平方數的話是多少)

---

try_2.py: O(n^(h/2)) O(n^(h/2))
* Runtime: 176 ms, faster than 88.53% of Python3 online submissions for Perfect Squares.
* Memory Usage: 15.1 MB, less than 5.00% of Python3 online submissions for Perfect Squares.

> bfs
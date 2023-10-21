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

> bfs: 去算每一次的剩餘的n的所有可能，用set去去除重複的情況

---

try_3.py: O(n^2) O(n)
* Runtime: 6668 ms, faster than 7.96% of Python3 online submissions for Perfect Squares.
* Memory Usage: 39.4 MB, less than 6.94% of Python3 online submissions for Perfect Squares.

> dfs + dp

---

try_4.py: O(n^2) O(n)
* Runtime: 3492 ms, faster than 55.06% of Python3 online submissions for Perfect Squares.
* Memory Usage: 14.3 MB, less than 61.36% of Python3 online submissions for Perfect Squares.

> bottom-up: 從底部往上算，目前的數字最少需要多少的步數，一路算到n，就可以保證n是最少的

---

try_5.py: O(n^2) O(n)

* Runtime: 4403 ms, faster than 42.34% of Python3 online submissions for Perfect Squares.
* Memory Usage: 14.3 MB, less than 85.95% of Python3 online submissions for Perfect Squares.

> coin change，要記得先預算square才不用每一次都要重算

---

try_6.py: O(n^2) O(n)

* Runtime: 5026 ms, faster than 28.88% of Python3 online submissions for Perfect Squares.
* Memory Usage: 14.3 MB, less than 73.06% of Python3 online submissions for Perfect Squares.

> coin change

---

try_7.py: O(n^2) O(n)

* Runtime: 1007 ms, faster than 70.55% of Python3 online submissions for Perfect Squares.
* Memory Usage: 15.6 MB, less than 21.75% of Python3 online submissions for Perfect Squares.

> bfs set

---

try_8.py: O(n*sqrt(n)) O(n)

* Runtime: 3019 ms, faster than 49.72% of Python3 online submissions for Perfect Squares.
* Memory Usage: 16.5 MB, less than 46.85% of Python3 online submissions for Perfect Squares.

> coin change

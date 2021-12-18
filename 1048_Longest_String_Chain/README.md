Question: https://leetcode.com/problems/longest-string-chain/

---

try_1.py: O(n) O(n)

* Runtime: 160 ms, faster than 68.29% of Python3 online submissions for Longest String Chain.
* Memory Usage: 14.7 MB, less than 80.92% of Python3 online submissions for Longest String Chain.

> 從最長的開始跑 (排序)
> 用queue set儲存每層找到的值(怕刪除後會有重複)
> 之後紀錄有找過的值，若第一次找過a，第二次找到a時，答案一定會比原本的小，所以就不用找這個字了
> 若答案已經比i大了，就不用再往下找了

---

try_2.py: O(n^2) O(n)

* Runtime: 1022 ms, faster than 16.69% of Python3 online submissions for Longest String Chain.
* Memory Usage: 14.9 MB, less than 44.25% of Python3 online submissions for Longest String Chain.

> coin change

---

try_3.py: O(n) O(n)

* Runtime: 196 ms, faster than 43.64% of Python3 online submissions for Longest String Chain.
* Memory Usage: 14.5 MB, less than 93.88% of Python3 online submissions for Longest String Chain.

> bfs set

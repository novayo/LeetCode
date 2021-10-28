Question: https://leetcode.com/problems/longest-string-chain/

---

try_1.py: O(n) O(n)

* Runtime: 160 ms, faster than 68.29% of Python3 online submissions for Longest String Chain.
* Memory Usage: 14.7 MB, less than 80.92% of Python3 online submissions for Longest String Chain.

> 從最長的開始跑 (排序)
> 用queue set儲存每層找到的值(怕刪除後會有重複)
> 之後紀錄有找過的值，若第一次找過a，第二次找到a時，答案一定會比原本的小，所以就不用找這個字了
> 若答案已經比i大了，就不用再往下找了
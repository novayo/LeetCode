Question: https://leetcode.com/problems/wiggle-sort/

---

try_1.py: O(nlogn) O(1)

* Runtime: 95 ms, faster than 55.83% of Python3 online submissions for Wiggle Sort.
* Memory Usage: 15 MB, less than 76.70% of Python3 online submissions for Wiggle Sort.

> sort 後
> i = 1, j = len // 2 => i, j交換後，再讓i+1, j交換, i+=1, j+=1

---

try_2.py: O(n) O(1)

* Runtime: 84 ms, faster than 97.35% of Python3 online submissions for Wiggle Sort.
* Memory Usage: 15.1 MB, less than 51.20% of Python3 online submissions for Wiggle Sort.

> 比較自己跟一格後的大小去做交換即可

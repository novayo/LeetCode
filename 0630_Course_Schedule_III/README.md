Question: https://leetcode.com/problems/course-schedule-iii/

---

try_1.py: O(n^2) O(n)

* TLE

> 排序後從頭開始選，並更新所有之前的情況（求最小），之後查看選了多少課即可。

---

try_2.py: O(nlogn) O(n)

* Runtime: 700 ms, faster than 67.07% of Python3 online submissions for Course Schedule III.
* Memory Usage: 19.4 MB, less than 51.09% of Python3 online submissions for Course Schedule III.

> 依照end排序過後，將跑過的課都選起來，只要總時間沒有超過當前end就算合理
>       
> 只要超過end，就將最大的start刪除直到合理，這部分可以用max heap
>       
> 因為每一次都將最長的start去除，因此就能保證可以greedy的取到最長
> 而且，排序end就能將時間也考慮進去，也就是先選最早消失的

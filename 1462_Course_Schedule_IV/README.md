Question: https://leetcode.com/problems/course-schedule-iv/

---

try_1: O(n^2) O(n)

* Runtime: 752 ms, faster than 84.44% of Python3 online submissions for Course Schedule IV.
* Memory Usage: 17.5 MB, less than 95.44% of Python3 online submissions for Course Schedule IV.

> 先做一次拓樸，把關係找出來，只是要多算一個prerequisites
>       
> A->B->C
> B的prerequisites有C
> A的prerequisites有B + C(B的prerequisites)
>       
> 之後去查詢queries = [a, b]
> b的prerequisites是否有a即可

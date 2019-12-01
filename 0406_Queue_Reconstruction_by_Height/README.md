Question: https://leetcode.com/problems/queue-reconstruction-by-height/
---

try_1.py: O(n^2)

* Runtime: 468 ms, faster than 21.12% of Python3 online submissions for Queue Reconstruction by Height.
* Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Queue Reconstruction by Height.

> straightforward => greedy

---

try_2.py: O(n)

* Runtime: 96 ms, faster than 96.14% of Python3 online submissions for Queue Reconstruction by Height.
* Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Queue Reconstruction by Height.

> thanks for being sorted, insert by k will be fine
> 因為已經排序好了，因此可以直接用第二個參數下去做排序 -> 翻譯：矮子插隊無所謂，反正高個子看不到

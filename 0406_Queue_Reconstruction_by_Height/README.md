Question: https://leetcode.com/problems/queue-reconstruction-by-height/
---
try_1.py: https://leetcode.com/submissions/detail/261545747/
(straightforward => greedy)

> Runtime: 460 ms, faster than 18.70% of Python3 online submissions for Queue Reconstruction by Height.
> Memory Usage: 14.2 MB, less than 5.88% of Python3 online submissions for Queue Reconstruction by Height.

try_2.py: https://leetcode.com/submissions/detail/261633846/
(thanks for being sorted, insert by k will be fine)
(因為已經排序好了，因此可以直接用第二個參數下去做排序 -> 翻譯：矮子插隊無所謂，反正高個子看不到)

> Runtime: 108 ms, faster than 94.12% of Python3 online submissions for Queue Reconstruction by Height.
> Memory Usage: 14.3 MB, less than 5.88% of Python3 online submissions for Queue Reconstruction by Height.

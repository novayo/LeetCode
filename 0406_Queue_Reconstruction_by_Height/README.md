Question: https://leetcode.com/problems/queue-reconstruction-by-height/
---
try_1.py: O(n^2) 444ms
> straightforward => greedy

try_2.py: O(n) 112ms
> thanks for being sorted, insert by k will be fine
> 因為已經排序好了，因此可以直接用第二個參數下去做排序 -> 翻譯：矮子插隊無所謂，反正高個子看不到

Question: https://leetcode.com/problems/longest-increasing-subsequence/

---

try_1.py: O(n^2) O(n)

* Runtime: 3368 ms, faster than 52.50% of Python3 online submissions for Longest Increasing Subsequence.
* Memory Usage: 14.6 MB, less than 76.52% of Python3 online submissions for Longest Increasing Subsequence.

> dp
> '''
>       暴力解的話，需要一直去往下看下一個的最大是多少，
>       因此可以用dp去存起來（存大於幾個人，自己算一個），並之後去查找就可以了，
>       只是這樣會有個bug，
>        就是 會不知道要抓後面誰的dp，
>       假設 5,10,11,6,7,8，那以5來說，在dp的時候，要抓10（dp=2）的還是抓6（dp=3）呢？
>       所以還是得去跑過後面的所有dp，
>       並且，
>       讓 >5的值的dp去做max就可以找到ans了，
>       就是要去測試 5,10  ;  5,11  ;  5,6  ;  5,7  ;  5,8 看哪個最大（因為dp是記自己大於幾人）。
>       ''' 

---

try_2.py: O(nlogn) O(n)

* Runtime: 56 ms, faster than 99.87% of Python3 online submissions for Longest Increasing Subsequence.
* Memory Usage: 14.6 MB, less than 76.52% of Python3 online submissions for Longest Increasing Subsequence.

> patient sort

---

try_3.py: O(nlogn) O(n)

* Runtime: 130 ms, faster than 72.25% of Python3 online submissions for Longest Increasing Subsequence.
* Memory Usage: 14.5 MB, less than 90.70% of Python3 online submissions for Longest Increasing Subsequence.

> patient sort

---

try_4.py: O(nlogn) O(n)

* Runtime: 68 ms, faster than 94.84% of Python3 online submissions for Longest Increasing Subsequence.
* Memory Usage: 14.8 MB, less than 17.01% of Python3 online submissions for Longest Increasing Subsequence.

> patient sort

---

try_5.py: O(nlogn) O(n)

* Runtime: 78 ms, faster than 88.46% of Python3 online submissions for Longest Increasing Subsequence.
* Memory Usage: 14.6 MB, less than 48.93% of Python3 online submissions for Longest Increasing Subsequence.

> patient sort

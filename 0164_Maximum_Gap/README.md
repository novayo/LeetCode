Question: https://leetcode.com/problems/maximum-gap/

---

try_1.py: O(n) O(n)

* Runtime: 1568 ms, faster than 31.99% of Python3 online submissions for Maximum Gap.
* Memory Usage: 41.1 MB, less than 18.41% of Python3 online submissions for Maximum Gap.

> bucket sort
> 	seperate nums into n-1 buckets, and answer will locate in 
>	min (in bucketN+1) - max (in bucketN) 	

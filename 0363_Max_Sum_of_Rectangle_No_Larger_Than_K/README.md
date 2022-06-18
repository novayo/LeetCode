Question: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

---

try_1.py: O(mn * mlogn) O(mn)

* Runtime: 9743 ms, faster than 5.23% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
* Memory Usage: 15.3 MB, less than 29.48% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.

> 2d maximum subarray

---

try_2.py: O(min(m,n)^2 * max(m,n) * log(max(m, n))) O(max(m, n))

* Runtime: 3526 ms, faster than 58.96% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
* Memory Usage: 15.4 MB, less than 7.46% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.

> optimize try_1.py by 
> 	1. duo to the time complexity in try_1.py is O(m^2*nlogn) => so transpose if height is greater than width
> 	2. It cost O(nlogn) time on calculating the 1-d strategy. We can do a standard kadane to reduce the runtime.

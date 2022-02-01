Question: https://leetcode.com/problems/subarray-sum-equals-k/

---

try_1.py: O(n) O(n)

* Runtime: 108 ms, faster than 91.35% of Python3 online submissions for Subarray Sum Equals K.
* Memory Usage: 16.2 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.

> sum(i,j) = sum(0,j) - sum(0,i)

---

try_2.py: O(n) O(n)

* Runtime: 272 ms, faster than 47.76% of Python3 online submissions for Subarray Sum Equals K.
* Memory Usage: 16.7 MB, less than 61.97% of Python3 online submissions for Subarray Sum Equals K.

> presum + hash table to store counting

---

try_3.py: O(n) O(n)

* Runtime: 304 ms, faster than 46.55% of Python3 online submissions for Subarray Sum Equals K.
* Memory Usage: 18.6 MB, less than 8.54% of Python3 online submissions for Subarray Sum Equals K.

> presum + two sum

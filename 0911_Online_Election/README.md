Question: https://leetcode.com/problems/online-election/

---

try_1.py: O(n^2 + nlogn) O(n)

* Runtime: 1340 ms, faster than 15.07% of Python3 online submissions for Online Election.
* Memory Usage: 19.7 MB, less than 17.47% of Python3 online submissions for Online Election.

> binary search + OrderedDict to solve recent problem

---

try_2.py: O(n + nlogn) O(n)

* Runtime: 948 ms, faster than 38.83% of Python3 online submissions for Online Election.
* Memory Usage: 19.8 MB, less than 12.37% of Python3 online submissions for Online Election.


> binary search + optimize LRU problem
> 	only vote a ticket at one time       
> 	so we are able to use a variable to store leader

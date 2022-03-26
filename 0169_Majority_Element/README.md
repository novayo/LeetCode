Question: https://leetcode.com/problems/majority-element/

---

try_1.py: O(n) O(n)
* Runtime: 164 ms, faster than 96.50% of Python3 online submissions for Majority Element.
* Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions for Majority Element.

> counter

---

try_2.py: O(nlogn) O(1)
* Runtime: 164 ms, faster than 96.50% of Python3 online submissions for Majority Element.
* Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions for Majority Element.

> 因為超過一半，所以sort過後，直接回傳中間

---

try_3.py: O(n) O(1)
* Runtime: 168 ms, faster than 91.15% of Python3 online submissions for Majority Element.
* Memory Usage: 15.1 MB, less than 7.14% of Python3 online submissions for Majority Element.

> Boyer-Moore Voting Algorithm
	> 間單來說，先分成兩派，一是超過半數的人（答案），二是剩下的（非答案），遇到答案就+1，非答案就-1
	> 所以先記第一個數字，之後遇到跟他相同的就counter+1，反之-1，最後記得的數字一定是答案

---

try_4.py: O(n) O(1)

* Runtime: 164 ms, faster than 96.98% of Python3 online submissions for Majority Element.
* Memory Usage: 15.3 MB, less than 97.76% of Python3 online submissions for Majority Element.

> candidate

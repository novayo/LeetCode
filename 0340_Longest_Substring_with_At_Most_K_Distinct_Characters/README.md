Question: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

---

try_1.py:
* Runtime: 80 ms, faster than 57.44% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
* Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.

> hash_table + sliding window

---

try_2.py:
* Runtime: 64 ms, faster than 91.67% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.

> hash_table + sliding window
	> store index in hash_table, we only care about the smallest index of item
	> So, when we have to update something, find out the smallest index and update i to that index + 1	

---

try_3.py: O(n) O(n)

* Runtime: 60 ms, faster than 98.18% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
* Memory Usage: 14.2 MB, less than 85.25% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.

> God solution

---

try_4.py: O(n) O(n)

* Runtime: 78 ms, faster than 84.50% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
* Memory Usage: 14.2 MB, less than 90.04% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.

> ordereddict => 最左邊的元素一定是最早hit的，所以只要有hit就move to end，超過長度後就pop top即可
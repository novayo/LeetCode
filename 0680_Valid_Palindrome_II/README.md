Question: https://leetcode.com/problems/valid-palindrome-ii/

---

try_1.py: O(n) O(n)

* TLE

> reverse first and loop s

---

try_2.py: O(n) O(1)

* Runtime: 483 ms, faster than 6.59% of Python3 online submissions for Valid Palindrome II.
* Memory Usage: 14.6 MB, less than 70.24% of Python3 online submissions for Valid Palindrome II.

> two pointer at start and end
> move closely until there're not the same
> try to move left first
> try to move right next

---

try_3.py: O(n) O(1)

* Runtime: 161 ms, faster than 64.20% of Python3 online submissions for Valid Palindrome II.
* Memory Usage: 14.5 MB, less than 70.24% of Python3 online submissions for Valid Palindrome II.

> try_2.py but check string

---

try_4.py: O(n) O(1)

* Runtime: 145 ms, faster than 58.29% of Python3 online submissions for Valid Palindrome II.
* Memory Usage: 16.8 MB, less than 98.31% of Python3 online submissions for Valid Palindrome II.

> Greedy

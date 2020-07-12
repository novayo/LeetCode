Question: https://leetcode.com/problems/palindrome-linked-list/

---

try_1.py: O(n) O(n)
* Runtime: 116 ms, faster than 13.94% of Python3 online submissions for Palindrome Linked List.
* Memory Usage: 31.7 MB, less than 6.56% of Python3 online submissions for Palindrome Linked List. 

> 直接拷貝一份，並把原本的給reverse，再去比較即可

---

try_2.py: O(n) O(n)
* Runtime: 84 ms, faster than 37.94% of Python3 online submissions for Palindrome Linked List.
* Memory Usage: 24.2 MB, less than 24.63% of Python3 online submissions for Palindrome Linked List.

> try_1 using list

---

try_3.py: O(n) O(1)
* Runtime: 68 ms, faster than 88.68% of Python3 online submissions for Palindrome Linked List. 
* Memory Usage: 24.1 MB, less than 40.20% of Python3 online submissions for Palindrome Linked List.

> 龜兔賽跑 + reverse

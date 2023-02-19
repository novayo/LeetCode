Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

---

try_1.py:
* Runtime: 7276 ms, faster than 10.34% of Python3 online submissions for Find All Anagrams in a String.
* Memory Usage: 14.8 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.

> intuition

---

try_2.py: O(26n) O(26)

* Runtime: 188 ms, faster than 58.95% of Python3 online submissions for Find All Anagrams in a String.
* Memory Usage: 15.1 MB, less than 82.03% of Python3 online submissions for Find All Anagrams in a String.

> two pointer with counter
> 	-> if not in p => delete counter, move i, j to next index
>	-> if in p => +1
> 	-> if exceed, move i
> 		-> if match, add answer and move i
> 	check counter is match or not in every loop

---

try_3.py: O(26n) O(26)

* Runtime: 116 ms, faster than 74.64% of Python3 online submissions for Find All Anagrams in a String.
* Memory Usage: 15.2 MB, less than 74.37% of Python3 online submissions for Find All Anagrams in a String.

> hash table
            
---

try_4.py: O(26n) O(26)

* Runtime: 380 ms, faster than 25.36% of Python3 online submissions for Find All Anagrams in a String.
* Memory Usage: 15.1 MB, less than 74.37% of Python3 online submissions for Find All Anagrams in a String.

> counter

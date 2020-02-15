Question: https://leetcode.com/problems/maximum-product-of-word-lengths/

---

try_1.py: O(n^2)
* Runtime: 412 ms, faster than 70.75% of Python3 online submissions for Maximum Product of Word Lengths.
* Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Maximum Product of Word Lengths.

> bit

---

try_2.py: O(n^2)
* Runtime: 184 ms, faster than 96.49% of Python3 online submissions for Maximum Product of Word Lengths.
* Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Product of Word Lengths.

> bit + hashmap
	> 因為相同的文字會有相同的轉換過的bit數字
	> 假設"a" 跟 "aaaaaaaaa"，會有一樣的數字，所以只要記得"aaaaaaaa"就好了（因為他比較長），這樣記錄下來，去比較的時候，雖然一樣是n^2，但是會有比較少的n

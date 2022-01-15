Question: https://leetcode.com/problems/implement-magic-dictionary/

---

try_1.py: O(n*len(word)) O(n*len(word))

* Runtime: 366 ms, faster than 25.48% of Python3 online submissions for Implement Magic Dictionary.
* Memory Usage: 18.4 MB, less than 13.00% of Python3 online submissions for Implement Magic Dictionary.

> set

---

try_2.py: O(n*len(word)) O(n*26)

* Runtime: 396 ms, faster than 22.68% of Python3 online submissions for Implement Magic Dictionary.
* Memory Usage: 18.2 MB, less than 28.82% of Python3 online submissions for Implement Magic Dictionary.

> trie + dfs to find out if changed

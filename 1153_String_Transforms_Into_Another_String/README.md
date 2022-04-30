Question: https://leetcode.com/problems/string-transforms-into-another-string/

---

try_1.py:
* Runtime: 28 ms, faster than 66.15% of Python3 online submissions for String Transforms Into Another String.
*Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for String Transforms Into Another String.

> hash table

---

try_2.py: O(n) O(26)

* Runtime: 33 ms, faster than 79.22% of Python3 online submissions for String Transforms Into Another String.
* Memory Usage: 13.9 MB, less than 65.28% of Python3 online submissions for String Transforms Into Another String.

* hash table => take care of a -> b, b->c, c->a => this case is nonlegal

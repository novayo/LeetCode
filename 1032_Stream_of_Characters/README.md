Question: https://leetcode.com/problems/stream-of-characters/

---

try_1.py: O(len(word) * len(words) + len(word) * num_of_query) time / O(len(word) * len(words))

* Runtime: 5405 ms, faster than 7.27% of Python3 online submissions for Stream of Characters.
* Memory Usage: 28.9 MB, less than 96.56% of Python3 online submissions for Stream of Characters.

> naive compare

---

try_2.py: O(len(word) * len(words) + len(word) * num_of_query) time / O(len(word) * len(words))

* Runtime: 904 ms, faster than 53.92% of Python3 online submissions for Stream of Characters.
* Memory Usage: 39.2 MB, less than 66.35% of Python3 online submissions for Stream of Characters.

> Trie
> same as try_1.py but return earlier

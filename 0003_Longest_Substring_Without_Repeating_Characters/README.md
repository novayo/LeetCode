Question: https://www.zhihu.com/question/19871785
---

try_1.py: O(n)

* Runtime: 48 ms, faster than 97.89% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.

> straightforward

---

try_2.py: O(n)

* Runtime: 80 ms, faster than 42.50% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

> sliding window

---

try_3.py: O(n) O(n)
* Runtime: 68 ms, faster than 51.43% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 14.3 MB, less than 58.62% of Python3 online submissions for Longest Substring Without Repeating Characters.

> sliding window + hash table

---

try_4.py: O(n) O(n)

* Runtime: 104 ms, faster than 27.61% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 14.2 MB, less than 80.82% of Python3 online submissions for Longest Substring Without Repeating Characters.

> sliding window + hash table

---

try_5.py: O(n) O(n)

* Runtime: 56 ms, faster than 85.03% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 14.4 MB, less than 25.13% of Python3 online submissions for Longest Substring Without Repeating Characters.

> instead of maintain the buffer dict(O(2n)), we check if the index is greater or equal than the index in buffer

---

try_6.py: O(n) O(n)

* Runtime: 114 ms, faster than 30.77% of Python3 online submissions for Longest Substring Without Repeating Characters.
* Memory Usage: 14.3 MB, less than 79.77% of Python3 online submissions for Longest Substring Without Repeating Characters.

> hash table + sliding window

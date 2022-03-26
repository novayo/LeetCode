Question: https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
---

try_1.py: O(n)

* Runtime: 552 ms, faster than 32.34% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
* Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

> straightforward

---

try_2.py:
* Runtime: 64 ms, faster than 95.81% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
* Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

> bisect

---

try_3.py: O(nlogn) O(n)

* Runtime: 84 ms, faster than 69.01% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
* Memory Usage: 15 MB, less than 19.88% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

> binary search find answer

---

try_4.py: O(n) O(n)

* Runtime: 183 ms, faster than 43.69% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
* Memory Usage: 14.6 MB, less than 73.54% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

> Because the freqency is small, we can use bucket sort.

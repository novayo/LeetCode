Question: https://leetcode.com/problems/evaluate-division/

---

try_1.py: O(n) O(n)

* Runtime: 28 ms, faster than 89.56% of Python3 online submissions for Evaluate Division.
* Memory Usage: 14.3 MB, less than 49.08% of Python3 online submissions for Evaluate Division.

> 建立雙向graph，找到對應點後，回傳路徑乘積

---

try_2.py: O(n) O(n)

* Runtime: 28 ms, faster than 89.23% of Python3 online submissions for Evaluate Division.
* Memory Usage: 14.3 MB, less than 76.66% of Python3 online submissions for Evaluate Division.

> same as try_1.py

---

try_2.py: O(n^3) O(n^2)

* Runtime: 36 ms, faster than 37.17% of Python3 online submissions for Evaluate Division.
* Memory Usage: 14.3 MB, less than 51.14% of Python3 online submissions for Evaluate Division.

> floyd warshall

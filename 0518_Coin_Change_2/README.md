Question: https://leetcode.com/problems/coin-change-2/

---

try_1.java:
* Runtime: 3 ms, faster than 71.08% of Java online submissions for Coin Change 2.
* Memory Usage: 36.5 MB, less than 75.98% of Java online submissions for Coin Change 2.

> dp

---

try_2.py: O(n*amount) O(amount)

* Runtime: 212 ms, faster than 62.52% of Python3 online submissions for Coin Change 2.
* Memory Usage: 14.3 MB, less than 95.19% of Python3 online submissions for Coin Change 2.

> dp
> 但不能把coin loop寫在裡面(try_3.py)，因為往前看的話，會重複算到 (1=1, 2=含1,2, 3=只需dp[2]+1 (因為會重複算到1+2 跟 2+1 算同一個))
> https://leetcode.com/problems/coin-change-2/discuss/176706/Beginner-Mistake%3A-Why-an-inner-loop-for-coins-doensn't-work-Java-Soln

---

try_4.py: O(n*amount) O(n*amount)

* Runtime: 532 ms, faster than 31.53% of Python3 online submissions for Coin Change 2.
* Memory Usage: 29.7 MB, less than 32.68% of Python3 online submissions for Coin Change 2.

> knapsack

---

try_5.py: O(n*amount) O(n*amount)

* Runtime: 790 ms, faster than 21.31% of Python3 online submissions for Coin Change 2.
* Memory Usage: 29.6 MB, less than 33.36% of Python3 online submissions for Coin Change 2.

> knapsack

---

try_6.py: O(n*m) O(n*m)

* Runtime: 553 ms, faster than 33.85% of Python3 online submissions for Coin Change 2.
* Memory Usage: 29.6 MB, less than 33.35% of Python3 online submissions for Coin Change 2.

> knapsack

---

try_7.py: O(m*n) O(m*n)

* Runtime: 509 ms, faster than 28.67% of Python3 online submissions for Coin Change II.
* Memory Usage: 152.1 MB, less than 18.36% of Python3 online submissions for Coin Change II.

> recursion

---

try_8.py: O(m*n) O(m)

> Runtime: 163 ms, faster than 71.54% of Python3 online submissions for Coin Change II.
* Memory Usage: 16.6 MB, less than 69.24% of Python3 online submissions for Coin Change II.

> dp

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
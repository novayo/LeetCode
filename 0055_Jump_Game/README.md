Question: https://leetcode.com/problems/jump-game/

---

try_1.py: O(n)
* Runtime: 84 ms, faster than 92.58% of Python3 online submissions for Jump Game.
* Memory Usage: 16 MB, less than 7.14% of Python3 online submissions for Jump Game.

> intuition

---

try_2.py: O(n)
* Runtime: 88 ms, faster than 80.60% of Python3 online submissions for Jump Game.
* Memory Usage: 16 MB, less than 7.14% of Python3 online submissions for Jump Game.

> check last pos

---

try_3.py: O(n)
* Runtime: 92 ms, faster than 36.58% of Python3 online submissions for Jump Game.
* Memory Usage: 15.9 MB, less than 95.77% of Python3 online submissions for Jump Game.

> 只要有數字，一定走得到結尾
> 因此只要尋找0，看是否目前"最遠到達index"能否超越此位置即可，且此位置不能為最後一位

---

try_4.py: O(n) O(1)

* Runtime: 588 ms, faster than 55.22% of Python3 online submissions for Jump Game.
* Memory Usage: 15.2 MB, less than 71.36% of Python3 online submissions for Jump Game.

> check last pos

---

try_5.py: O(n) O(1)

* Runtime: 769 ms, faster than 36.85% of Python3 online submissions for Jump Game.
* Memory Usage: 15.3 MB, less than 56.15% of Python3 online submissions for Jump Game.

> dp

---

try_6.py: O(n) O(1)

* Runtime: 495 ms, faster than 39.67% of Python3 online submissions for Jump Game.
* Memory Usage: 17.7 MB, less than 54.90% of Python3 online submissions for Jump Game.

> greedy

---

try_7.py: O(n*n) O(n)

* Runtime: 9099 ms, faster than 5.00% of Python3 online submissions for Jump Game.
* Memory Usage: 31.6 MB, less than 5.06% of Python3 online submissions for Jump Game.

> recr + memo

---

try_8.py: O(n) O(n)

* Runtime: 1310 ms, faster than 18.87% of Python3 online submissions for Jump Game.
* Memory Usage: 17.6 MB, less than 23.02% of Python3 online submissions for Jump Game.

> dp

Question: https://leetcode.com/problems/24-game/

---

try_1.py: O(4^4) O(4^4)

* Runtime: 1421 ms, faster than 5.04% of Python3 online submissions for 24 Game.* 
Memory Usage: 13.9 MB, less than 40.83% of Python3 online submissions for 24 Game.

> choose any two elements to do operation and push into cards then do recursion

---

try_2.py: O(4*4! * 4^4) O(4^4)

* Runtime: 1042 ms, faster than 6.20% of Python3 online submissions for 24 Game.* 
Memory Usage: 13.9 MB, less than 40.83% of Python3 online submissions for 24 Game.

> next permutation, and use recrsion to find out all the possibilites

---

try_3.py: O(4*(C(4, 1)+C(4,2)+C(4,3)) * 4^4) O(4^4)

* Runtime: 3803 ms, faster than 5.04% of Python3 online submissions for 24 Game.
* Memory Usage: 14.2 MB, less than 10.72% of Python3 online submissions for 24 Game.

> split into left (length from 1~n-1) right (length from n-1~1), and try to do operation

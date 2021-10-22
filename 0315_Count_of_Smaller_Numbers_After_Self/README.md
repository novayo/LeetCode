Question: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

---

try_1.py: O(n^2*logn) O(n)

* Runtime: 5136 ms, faster than 20.73% of Python3 online submissions for Count of Smaller Numbers After Self.
* Memory Usage: 32.6 MB, less than 85.00% of Python3 online submissions for Count of Smaller Numbers After Self.

> binary search to handle sorted list and find number of smaller elements

---

try_2.py: O(nlogn) O(n)

* Runtime: 2484 ms, faster than 68.29% of Python3 online submissions for Count of Smaller Numbers After Self.
* Memory Usage: 35.3 MB, less than 37.40% of Python3 online submissions for Count of Smaller Numbers After Self.

> binary indexed tree to optimize try_1.py

---

try_3.py: O(nlogn) O(n)

* Runtime: 4052 ms, faster than 41.56% of Python3 online submissions for Count of Smaller Numbers After Self.
* Memory Usage: 35.1 MB, less than 55.66% of Python3 online submissions for Count of Smaller Numbers After Self.

> 一般來說，binary indexed tree 用於presum
> 但 此題可以先sort找出每個值應當放的位置，從尾巴依序依照index放入tree中，update時delta=1 => 代表目前小於此數的個數是多少
Question: https://leetcode.com/problems/first-missing-positive/

---

try_1.py:
* Runtime: 24 ms, faster than 99.07% of Python3 online submissions for First Missing Positive.
* Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

> using set

---

try_2.py: O(n) O(1)

* Runtime: 936 ms, faster than 66.83% of Python3 online submissions for First Missing Positive.
* Memory Usage: 60 MB, less than 93.03% of Python3 online submissions for First Missing Positive.

> two pass
> one for swapping the value to mapping index
> one for searching answer

---

try_3.py: O(n) O(1)

* Runtime: 976 ms, faster than 53.68% of Python3 online submissions for First Missing Positive.
* Memory Usage: 60.2 MB, less than 79.91% of Python3 online submissions for First Missing Positive.

> 讓index為value的位置變成-的，之後檢查-的即可
> 1. 先查看是否答案是1
> 2. 將超過範圍的值改成1 (1~len(nums)-1)
> 3. 將對應value的index改成負的
> 4. loop第一個正的

---

try_4.py: O(n) O(1)

* Runtime: 317 ms, faster than 51.09% of Python3 online submissions for First Missing Positive.
* Memory Usage: 24 MB, less than 98.50% of Python3 online submissions for First Missing Positive.

> Mark

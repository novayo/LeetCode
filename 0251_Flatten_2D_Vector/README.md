Question: https://leetcode.com/problems/flatten-2d-vector/

---

try_1.py: O(n) O(n)
* Runtime: 80 ms, faster than 91.01% of Python3 online submissions for Flatten 2D Vector.
* Memory Usage: 19.8 MB, less than 15.56% of Python3 online submissions for Flatten 2D Vector.

> 直接用一個list存起來並用一個index去只向它
> 但這個方法會用到額外的記憶體 以及 會去跑額外的時間（建立list時）
> 因此這方法不好

---

try_2.py: O(1) O(1)
* Runtime: 92 ms, faster than 55.38% of Python3 online submissions for Flatten 2D Vector.
* Memory Usage: 19.6 MB, less than 44.89% of Python3 online submissions for Flatten 2D Vector.

> 用這兩個變數來指向對應的index，
> 如此一來可以減少建立list的時間，也可以節省記憶體

---

try_3.py: O(n) O(n)

* Runtime: 132 ms, faster than 24.68% of Python3 online submissions for Flatten 2D Vector.
* Memory Usage: 19.3 MB, less than 63.83% of Python3 online submissions for Flatten 2D Vector.

> flatten first, use iteration

Question: https://leetcode.com/problems/insert-delete-getrandom-o1/

---

try_1.py: O(n) O(n)

* Runtime: 444 ms, faster than 9.10% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 18.9 MB, less than 7.21% of Python3 online submissions for Insert Delete GetRandom O(1).

> getRandom 為 O(n)

---

try_2.py: O(1) O(n)

* Runtime: 92 ms, faster than 87.68% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 18.5 MB, less than 60.25% of Python3 online submissions for Insert Delete GetRandom O(1).

> list存值，dict存key=值，value=index，因此只要取亂數時，從list取就好，但remove要注意list跟dict的index要同步

---

try_3.py: O(1) O(n)

* Runtime: 1728 ms, faster than 5.06% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 61.6 MB, less than 83.66% of Python3 online submissions for Insert Delete GetRandom O(1).

> set for insert and remove, random.sample for getRandom

---

try_4.py: O(1) O(n)

* Runtime: 436 ms, faster than 78.49% of Python3 online submissions for Insert Delete GetRandom O(1).
* Memory Usage: 61.9 MB, less than 45.49% of Python3 online submissions for Insert Delete GetRandom O(1).

> 用hash紀錄每個值的index (insert、remove 檢查時是否存在時 => O(1))
> 用arr紀錄值 (getRandom 直接隨機找一個 => O(1))
> insert => append即可，同時記錄index => O(1)
> remove => 跟最後交換，再pop，同時更新index => O(1)
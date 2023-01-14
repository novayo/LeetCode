Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

---

try_1.py:
* Runtime: 56 ms, faster than 98.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 13.9 MB, less than 74.71% of Python3 online submissions for Best Time to Buy and Sell Stock.

> straightforward

---

try_2.py:
* Runtime: 56 ms, faster than 98.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 13.8 MB, less than 93.10% of Python3 online submissions for Best Time to Buy and Sell Stock.

> one pass
> 	* store min price and find max profit as looping

---

try_3.py: O(n) O(n)

* Runtime: 1128 ms, faster than 49.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25.2 MB, less than 53.99% of Python3 online submissions for Best Time to Buy and Sell Stock

> dp紀錄0~當前位置的最小值是誰 O(n)
> 之後再跑一次loop去找最大profit即可

---

try_4.py: O(n) O(n)

* Runtime: 2619 ms, faster than 5.01% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25 MB, less than 42.99% of Python3 online submissions for Best Time to Buy and Sell Stock.

> dp

---

try_5.py: O(n) O(1)

* Runtime: 1098 ms, faster than 76.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25 MB, less than 85.93% of Python3 online submissions for Best Time to Buy and Sell Stock.

> greedy

---

try_6.py: O(n) O(n)

* Runtime: 1317 ms, faster than 50.54% of Python3 online submissions for Best Time to Buy and Sell Stock.
* Memory Usage: 25.1 MB, less than 6.82% of Python3 online submissions for Best Time to Buy and Sell Stock.

> dp: 0~index的最小值是誰少

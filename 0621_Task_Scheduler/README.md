Question: https://leetcode.com/problems/task-scheduler/

---

try_1.py:
* Runtime: 548 ms, faster than 49.11% of Python3 online submissions for Task Scheduler.
* Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Task Scheduler.

> straightforward
> 	* n個分成一組，不夠n的就算要補幾個idle

---

try_2.py:
* Runtime: 416 ms, faster than 93.14% of Python3 online submissions for Task Scheduler.
* Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Task Scheduler.

> find a formula
> 	* (拿最多的符號的個數出來 - 1)*(n+1) + 總共有幾個最多符號的個數
>	* 但是要注意如果算出來的值 < tasks的數量，那就要回傳tasks的數量

---

try_3.py:

* Runtime: 662 ms, faster than 30.33% of Python3 online submissions for Task Scheduler.
* Memory Usage: 14.7 MB, less than 84.65% of Python3 online submissions for Task Scheduler.

> 先排滿，再扣除

---

try_4.py: O(nlogn) O(n)

* Runtime: 485 ms, faster than 78.52% of Python3 online submissions for Task Scheduler.
* Memory Usage: 14.3 MB, less than 52.78% of Python3 online submissions for Task Scheduler.

> greedy

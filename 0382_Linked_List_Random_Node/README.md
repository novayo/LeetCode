Question: https://leetcode.com/problems/linked-list-random-node/

---

try_1.py: O(n) O(n)

* Runtime: 96 ms, faster than 66.39% of Python3 online submissions for Linked List Random Node.
* Memory Usage: 17.5 MB, less than 23.43% of Python3 online submissions for Linked List Random Node.

> dump to list

---

try_2.py: O(n) O(1)

* Runtime: 84 ms, faster than 80.13% of Python3 online submissions for Linked List Random Node.
* Memory Usage: 17.4 MB, less than 58.31% of Python3 online submissions for Linked List Random Node.

> loop all values
> 	index 0 vs 1~end => 1/2 to choose 0
> 	index 1 vs 2~end => 1/3 to choose 1
> 	index 2 vs 3~end => 1/4 to choose 2
> if hit => update choose value

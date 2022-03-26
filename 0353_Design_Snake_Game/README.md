Question: https://leetcode.com/problems/design-snake-game/

---

try_1.py: O(1) O(len(food))

* Runtime: 280 ms, faster than 42.95% of Python3 online submissions for Design Snake Game.
* Memory Usage: 15.6 MB, less than 91.79% of Python3 online submissions for Design Snake Game.

> 用dict存 並 編號（當前時間）（key: time, value: pos），set 存pos方邊in dict
> 編號超過就del，只需紀錄最小值即可
> 每動一步時間+1
> 若吃到食物則新增食物位置
> 超出邊界 或 in dict則return -1 => game flag

---

try_2.py: O(1) O(n), n refers to length of food

* Runtime: 282 ms, faster than 74.15% of Python3 online submissions for Design Snake Game.
* Memory Usage: 15.6 MB, less than 94.39% of Python3 online submissions for Design Snake Game.

> deque

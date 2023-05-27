Question: https://leetcode.com/problems/stone-game-iv/

---

try_1.py: O(n*sqrt(n)) O(n)
* Runtime: 772 ms, faster than 79.61% of Python3 online submissions for Stone Game IV.
* Memory Usage: 14.9 MB, less than 44.32% of Python3 online submissions for Stone Game IV.

> dp[i] = 為true or false => 輪到誰，誰就是true or false
> 因為另一個人會聰明的選擇
>       
> 所以 就變成去找說，因為都是Alex先選擇，所以就看目前的dp[n去減平方數]有沒有等於False，代表Alex選擇了此平方數之後，Bob絕對會輸，有的話這格就為True，否則為False
> 同時可以建立平方數的表

---

try_2.py: O(n*sqrt(n)) O(n)

* Runtime: 2611 ms, faster than 32.80% of Python3 online submissions for Stone Game IV.
* Memory Usage: 14.8 MB, less than 87.34% of Python3 online submissions for Stone Game IV.

> 往前找看是否 在此選擇下，下一個人為False

---

try_3.py: O(n*sqrt(n)) O(n)

* Runtime: 8277 ms, faster than 5.02% of Python3 online submissions for Stone Game IV.
* Memory Usage: 197.5 MB, less than 5.03% of Python3 online submissions for Stone Game IV.

> min max recursion

Question: https://leetcode.com/problems/network-delay-time/

---

try_1.py: O(V^V + ElogE) O(V+E)

* Runtime: 1185 ms, faster than 7.55% of Python3 online submissions for Network Delay Time.
* Memory Usage: 17.7 MB, less than 5.35% of Python3 online submissions for Network Delay Time.

> 這題是找最少走到所有點的時間 => 可以用圖論解 => dijkstra, bellman ford, floyd warshall

---

try_2.py: O(E+VlogV) O(V+E)

* Runtime: 523 ms, faster than 44.55% of Python3 online submissions for Network Delay Time.
* Memory Usage: 16.2 MB, less than 50.21% of Python3 online submissions for Network Delay Time.

> dijkstra

---

try_3.py: O(VE) O(VE)

* Runtime: 480 ms, faster than 59.48% of Python3 online submissions for Network Delay Time.
* Memory Usage: 16.3 MB, less than 25.28% of Python3 online submissions for Network Delay Time.

> bellman ford

---

try_4.py: O(V^3) O(V^2)

* Runtime: 1200 ms, faster than 7.47% of Python3 online submissions for Network Delay Time.
* Memory Usage: 16.1 MB, less than 91.42% of Python3 online submissions for Network Delay Time.

> floyd warshall

---

try_5.py: O(VlogV) O(V)

* Runtime: 402 ms, faster than 99.66% of Python3 online submissions for Network Delay Time.
* Memory Usage: 18.6 MB, less than 56.29% of Python3 online submissions for Network Delay Time.

> dijkstra

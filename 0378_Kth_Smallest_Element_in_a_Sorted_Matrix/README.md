Question: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
---

try_1.py: O(nlgn)

* Runtime: 176 ms, faster than 97.82% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
* Memory Usage: 18.7 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

> straightforward

---

try_2.py: O(klogn)

* Runtime: 272 ms, faster than 11.71% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
* Memory Usage: 25.8 MB, less than 5.58% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

> 找到目前最小後(priority queue)，加入右下兩個的資訊到queue內

---

try_3.py: O(klogn)

* Runtime: 288 ms, faster than 10.53% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
* Memory Usage: 20.7 MB, less than 9.65% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

> try_2優化: 找出最小之後，只須看下面即可，因為右邊的會比右上的來的大，所以不考慮加入

---

try_4.py: O(klogn)

* Runtime: 192 ms, faster than 60.29% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
* Memory Usage: 20.2 MB, less than 19.69% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

> 把所有質撈出來後，再去取得第k個

---

try_5.py: O(klogn) O(n)

* Runtime: 200 ms, faster than 59.31% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
* Memory Usage: 20 MB, less than 78.34% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

> 用prioirty queue紀錄每列的最左邊的值,每次取出最小, 並讓該位置的index+1, 這樣只需要取k次 

Question: https://leetcode.com/problems/maximum-length-of-repeated-subarray/

---

try_1.py: O(m*n) O(m)

* Runtime: 6836 ms, faster than 6.07% of Python3 online submissions for Maximum Length of Repeated Subarray.
* Memory Usage: 200.2 MB, less than 5.76% of Python3 online submissions for Maximum Length of Repeated Subarray.

> dp

---

try_2.py: (nlogn) O(n)

* Runtime: 428 ms, faster than 96.41% of Python3 online submissions for Maximum Length of Repeated Subarray.
* Memory Usage: 17.4 MB, less than 80.66% of Python3 online submissions for Maximum Length of Repeated Subarray.

> 找出長度n的Ａ的所有可能(set) => 再看B的所有可能有沒有存在於setA中
> 用長度去切binary,反正長度3有subarray符合的話，長度1~2就不用看了

---

try_3.py: O(m*n) O(m*n)

* Runtime: 6711 ms, faster than 15.12% of Python3 online submissions for Maximum Length of Repeated Subarray.
* Memory Usage: 39.5 MB, less than 37.83% of Python3 online submissions for Maximum Length of Repeated Subarray.

> simple LCS

---

try_4.py: O(nlogn) O(n)

* Runtime: 558 ms, faster than 94.38% of Python3 online submissions for Maximum Length of Repeated Subarray.
* Memory Usage: 17.5 MB, less than 81.69% of Python3 online submissions for Maximum Length of Repeated Subarray.

> binary search + sliding window

---

try_5.py: O(mn) O(min(m,n))

* Runtime: 2248 ms, faster than 28.88% of Python3 online submissions for Maximum Length of Repeated Subarray.
* Memory Usage: 16.3 MB, less than 93.66% of Python3 online submissions for Maximum Length of Repeated Subarray.

> dp optimized

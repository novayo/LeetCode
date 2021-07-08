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

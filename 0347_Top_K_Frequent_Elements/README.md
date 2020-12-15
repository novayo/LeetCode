Question: https://leetcode.com/problems/top-k-frequent-elements/

---

try_1.py: O(nlogn)
* Runtime: 108 ms, faster than 61.19% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.5 MB, less than 9.05% of Python3 online submissions for Top K Frequent Elements.

> 用dictionary去儲存每個值出現的次數，排序value之後抓出對應的key即可。
> sort用的是timsort，因此時間複雜度為nlogn

---

try_2.py: O(nlogn)
* Runtime: 92 ms, faster than 92.79% of Python3 online submissions for Top K Frequent Elements.
* Memory Usage: 18.9 MB, less than 16.31% of Python3 online submissions for Top K Frequent Elements.

> hash table + sort
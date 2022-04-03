Question: https://leetcode.com/problems/minimum-falling-path-sum/

---

try_1.py: O(3n) O(1)

* Runtime: 181 ms, faster than 22.05% of Python3 online submissions for Minimum Falling Path Sum.
* Memory Usage: 15.2 MB, less than 37.48% of Python3 online submissions for Minimum Falling Path Sum.

> 從倒數第二列開始，每個元素找下一列的左中右取最小，一路往上加，最後找出答案即可
        
---

try_2.py: O(n) O(1)

* Runtime: 152 ms, faster than 82.31% of Python3 online submissions for Minimum Falling Path Sum.
* Memory Usage: 14.9 MB, less than 25.28% of Python3 online submissions for Minimum Falling Path Sum.

> dp

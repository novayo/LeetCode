Question: https://leetcode.com/problems/remove-duplicate-letters/

---

try_1.py: O(26n) O(n)

* Runtime: 48 ms, faster than 53.20% of Python3 online submissions for Remove Duplicate Letters.
* Memory Usage: 14 MB, less than 87.76% of Python3 online submissions for Remove Duplicate Letters.

> greedy: https://leetcode.com/problems/remove-duplicate-letters/discuss/76766/Easy-to-understand-iterative-Java-solution
> 設定底線，一定有一個答案會在start~第一個紅線之一出現

---

try_2.py: O(n) O(n)

* Runtime: 32 ms, faster than 95.30% of Python3 online submissions for Remove Duplicate Letters.
* Memory Usage: 14.1 MB, less than 87.76% of Python3 online submissions for Remove Duplicate Letters.

> 紀錄每個char的最後一個位置
> stack的順序為答案
>       
> 跑s => 如果s[i]比stack[-1]小 & i後面還有此字母 => 那當然要把s[i]擺在前面呀，所以pop stack
>     => 再append到stack內

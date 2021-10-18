Question: https://leetcode.com/problems/unique-binary-search-trees/

---

try_1.py: O(n) O(n)

* Runtime: 24 ms, faster than 93.40% of Python3 online submissions for Unique Binary Search Trees.
* Memory Usage: 14.2 MB, less than 99.95% of Python3 online submissions for Unique Binary Search Trees.

> recursion
> 長度為n的bst能有k種組合，因此只要去計算長度為n中，0~n-1分別當頭的個數的總和是多少即可

---

try_2.py: O(n^2) O(n)

* Runtime: 54 ms, faster than 10.84% of Python3 online submissions for Unique Binary Search Trees.
* Memory Usage: 14.1 MB, less than 73.70% of Python3 online submissions for Unique Binary Search Trees.

> dp
> 假設n=3 => 1當頭時，2個數排列、2當頭時，左1個數排列*右1個數排列、3當頭時，2個數排列 => 總和是2+1+2=5 => 可得知3個數排列組合為5
> n=4 => 1當頭時，3個數排列、2當頭時，1*2個數排列、3當頭時，1*2個數排列、4當頭時，3個數排列 => 總和是5+2+2+5=14 => 可得知4個數排列組合為14

Question: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

---

try_1.py: O(n) O(1)

* Runtime: 912 ms, faster than 61.69% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.
* Memory Usage: 15 MB, less than 73.69% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.

> 切入點：答案只會有以下兩種010101 or 101010，所以可以把每一種可能都找過(Type-1)，並計算答案，也就是有幾個不同(Type-2)
> 所以，使用sliding window就可以不用重複算值 => 時間複雜度降為O(n)

---

try_2.py: O(n) O(1)

* Runtime: 548 ms, faster than 87.62% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.
* Memory Usage: 14.9 MB, less than 91.16% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.

> 優化try_1.py，長度偶數可以直接算

---

try_3.py: O(n) O(1)

* Runtime: 1246 ms, faster than 48.63% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.
* Memory Usage: 14.8 MB, less than 98.08% of Python3 online submissions for Minimum Number of Flips to Make the Binary String Alternating.

> sliding window
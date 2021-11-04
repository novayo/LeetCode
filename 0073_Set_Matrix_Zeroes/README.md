Question: https://leetcode.com/problems/set-matrix-zeroes/

---

try_1.py:
* Runtime: 128 ms, faster than 96.50% of Python3 online submissions for Set Matrix Zeroes.
* Memory Usage: 13.3 MB, less than 97.44% of Python3 online submissions for Set Matrix Zeroes.

> using set to implement O(m + n) space

---

try_2.py: O(n^2) O(1)
* Runtime: 132 ms, faster than 88.27% of Python3 online submissions for Set Matrix Zeroes.
* Memory Usage: 14.4 MB, less than 5.13% of Python3 online submissions for Set Matrix Zeroes.

> O(1) solution

---

try_3.py: O(n) O(n)

* Runtime: 124 ms, faster than 92.70% of Python3 online submissions for Set Matrix Zeroes.
* Memory Usage: 15 MB, less than 74.44% of Python3 online submissions for Set Matrix Zeroes.

> 遇到0，把相關的位置改成其他值，遇到0的時候跳過 => 先記錄要變成0的row col

---

try_4.py: O(n) O(1)

* Runtime: 132 ms, faster than 65.25% of Python3 online submissions for Set Matrix Zeroes.
* Memory Usage: 15.2 MB, less than 46.63% of Python3 online submissions for Set Matrix Zeroes.

> in-place
> 把要改變的row 跟 col 先在最上跟最左記錄起來
> 再把最上=0的行全改成0
> 再把最左=0的列全改成0
>       
> 最後判斷[0][0]是否為0，更新最上跟最左為0
> 如果原本最上或最左有0，也要更新最上為0或最左為0

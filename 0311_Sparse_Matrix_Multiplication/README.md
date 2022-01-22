Question: https://leetcode.com/problems/sparse-matrix-multiplication/

---

try_1.py: O(n) O(n)

* Runtime: 420 ms, faster than 5.09% of Python3 online submissions for Sparse Matrix Multiplication.
* Memory Usage: 14.8 MB, less than 11.07% of Python3 online submissions for Sparse Matrix Multiplication.

> matrix multiplication

---

try_2.py: O(n) O(n)

* Runtime: 77 ms, faster than 58.84% of Python3 online submissions for Sparse Matrix Multiplication.
* Memory Usage: 14.9 MB, less than 11.07% of Python3 online submissions for Sparse Matrix Multiplication.

> mat1 記得每列有值的位置
> mat2 記得每行有值的位置
> 看答案的(i, j) => 找出對應的位置是否有值 => i=>mat1[i][0:j], j=>mat2[0:i][j]
> 	=> 然後去看說，有沒有對應的index是有值的，有的話就相乘

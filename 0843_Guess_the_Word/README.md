Question: https://leetcode.com/problems/guess-the-word/

---

try_1.py: O(n)

* Runtime: 24 ms, faster than 97.06% of Python3 online submissions for Guess the Word.
* Memory Usage: 14.4 MB, less than 28.92% of Python3 online submissions for Guess the Word.

> random
> https://drive.google.com/file/d/127443bFPlnTcxOcifL6CHCZQhFPH9bYJ/view?usp=sharing

---

try_2.py: O(n^2)

* Runtime: 68 ms, faster than 18.21% of Python3 online submissions for Guess the Word.
* Memory Usage: 14.3 MB, less than 80.18% of Python3 online submissions for Guess the Word.

> 選出相關度最高的去猜，去除random機制

---

try_3.py: O(n)

* Runtime: 32 ms, faster than 74.16% of Python3 online submissions for Guess the Word.
* Memory Usage: 14.4 MB, less than 55.27% of Python3 online submissions for Guess the Word.

> optimize try_2.py
> calculate frequency of character on the position to represent the score

---

try_4.py: O(10)

* Runtime: 24 ms, faster than 97.55% of Python3 online submissions for Guess the Word.
* Memory Usage: 14.3 MB, less than 55.23% of Python3 online submissions for Guess the Word.

> random 找法(後續可以先找出相關性最多的下去猜，這樣可以省比較少時間)

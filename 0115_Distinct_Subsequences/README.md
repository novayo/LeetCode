Question: https://leetcode.com/problems/distinct-subsequences/

---

try_1.py: O(s*t) O(s*t)

* Runtime: 322 ms, faster than 58.99% of Python3 online submissions for Distinct Subsequences.
* Memory Usage: 71.2 MB, less than 32.92% of Python3 online submissions for Distinct Subsequences.

> s = 'rabbbit'
> t = 'rabbit'
> 從b開始，去紀錄後面有幾個it
> 有可能會有重複的b，所以要同時記得此b跟it的個數+之前的bit個數
```python=
'''
s[j]
rabbbit
1111111  t
1111110  it
3332100  bit   t[i]
3331000  bbit
3300000  abbit
3000000  rabbit
'''
```

---

try_2.py: O(s*t) O(2t)

* Runtime: 208 ms, faster than 78.33% of Python3 online submissions for Distinct Subsequences.
* Memory Usage: 14.4 MB, less than 85.55% of Python3 online submissions for Distinct Subsequences.

> Space optimized try_1.py
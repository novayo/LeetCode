Question: https://leetcode.com/problems/implement-rand10-using-rand7/

---

try_1.py: 

* Runtime: 1080 ms, faster than 14.04% of Python3 online submissions for Implement Rand10() Using Rand7().
* Memory Usage: 16.8 MB, less than 37.62% of Python3 online submissions for Implement Rand10() Using Rand7().

> 用rand7 + 3 => 取得4~10 => 每個機率1/7
> 用(rand7) % 3 + 1 => 取得1~3 => 每個機率1/3 (但1會多一次，要濾掉)
> 用rand7去模擬30%的情況 
>     => 取得1~3 => 這樣每個值的機率為 30% * 1/3 = 1/10
>     => 取得4~10=> 這樣每個值的機率為 70% * 1/7 = 1/10
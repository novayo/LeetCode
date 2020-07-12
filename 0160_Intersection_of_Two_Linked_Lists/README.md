Question: https://leetcode.com/problems/intersection-of-two-linked-lists/

---

try_1.py: O(m+n) O(1)
* Runtime: 164 ms, faster than 91.14% of Python3 online submissions for Intersection of Two Linked Lists.
* Memory Usage: 28.9 MB, less than 88.59% of Python3 online submissions for Intersection of Two Linked Lists.

> a往下跑A，b往下跑B
> 但是 A跟B的長度可能不同
> 因此，讓a走完之後走B，讓b走完之後走a，在這之中去看是否有相同的node即可
        
> 原理是因為
> a走完A之後走B，b走完B之後走A，
> 就代表讓a走了A+B，b也走了A+B，此時的長度就都走得一樣了
        
> 換句話說
> 就是讓 左圖的 B折上去A的前面，讓A折下來B的前面
> A: "b1->b2->b3"->a1->a2
> B: "a1->a2"->b1->b2->b3
        
> 這樣就轉換題目成長度相同的兩個linkedlist去跑了

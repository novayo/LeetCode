Question: https://leetcode.com/problems/max-stack/

---

try_1.py: O(n) O(n)

* Runtime: 168 ms, faster than 61.01% of Python3 online submissions for Max Stack.
* Memory Usage: 16.8 MB, less than 28.68% of Python3 online submissions for Max Stack.

> two stack
> one for normal, the other is for max_stack

---

try_2.py: O(logn) O(n)

* Runtime: 192 ms, faster than 46.88% of Python3 online submissions for Max Stack.
* Memory Usage: 17.4 MB, less than 6.41% of Python3 online submissions for Max Stack.

> [why we choose hash structure and linkedlist]
> for popMax 
> 	=> if we use list, the delete ops will be O(n)
> 	=> but, if we use linked list, the delete ops will be O(n) (for search)
> 	=> so, we have to use a 'hash' to store and get nodes => popMax (O(1) for search & delete)
>     
> [why we choose treemap]
> for peekMax/popMax
> 	=> we want a sorted hash structure to get the max element
> 	=> hash-table is not suitable => it's hashed but not sorted
> 	=> orderedDict is not suitable => it's hashed and ordered but not sorted
> 	=> treemap is suitable => it's hashed and sorted
>
> [linkedlist]
> for push/pop/top
> 	=> we can maintain self.last to make it done => O(1)
>       
> In the end, doubly linked list & treemap will speed up the time complexity to O(logn)
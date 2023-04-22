# **Python**

## **Basic**
<br/>

### Operator
    3 /  2 = 1.5    // float
    3 // 2 = 1      // integer
    3 ** 2 = 9      // power
### Slice
    a = 'apple'
    a[3] = 'l'
    a[0:4:1] = 'appl'
    a[0:4:2] = 'ap'     // from a[0] to a[4] get every 2 char
    a[::-1] = 'elppa'   // reverse
    
### Split
    a = 'a b@c'
    a.split() = ['a','b@c']     // split by ' '
    a.split('@') = ['a b','c']  // split by '@'

### Reversed
    list(reversed('Runoob')) = ['b', 'o', 'o', 'n', 'u', 'R']
    list(reversed(range(5,9))) = [8, 7, 6, 5]
---
<br/>

## **Logic Control**
<br/>

### For loop
    words = ['a','b','c']

    for a in words:
        print(a)
    for a in enumerate(words):  //enumerate
        print(a)
    for a in iter(words):       //iterator
        print(a)
    for a in range(len(words)): //range
        print(words[a])
### If Not

    lst = []
    if not lst      //check if empty
    if not 1 in lst //check if not contain 1
---
<br/>

## **Data Structer**
<br/>

### ListNode
> Definition for singly-linked list
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
list1 = Optional[LintNode]
```

### Deque
> Definition
```
from collections import deque
     
de = deque(['a','b','c'])
```
> pop, append
```
de.pop()
de.popleft()
de.append()
de.appendleft()
```
>Accessing Items
```
de.index(ele, beg, end) # return firstIndex of ${ele} searching from ${beg} to ${end}
de.insert(i,ele)        # insert ${ele} at index ${i}
de.count(ele)           # count the number of ${ele} in deque
de.remove(ele)          # remove the first occurs ${ele} in deque
de[0]                   # front element  
de[-1]                  # back element
```
> Others operations
```
de.extend()
de.extendleft()
de.rotate()
de.reverse()
```


# Python

## Basic

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
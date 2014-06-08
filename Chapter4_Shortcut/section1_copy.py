#!/usr/bin/env python
# * coding:utf-8 *

## sharrow copy
# import copy
# new_list = copy.copy(existing_list)

## deep copy
# import copy
# new_list_of_dicts = copy.deepcopy(exisiting_list_of_dicts)
#

## 基本はsharrowCopy

# >>> a=[1,2,3]
# >>> b=a
# >>> b.append(8)
# >>> print a,b
# [1, 2, 3, 8] [1, 2, 3, 8]


## deepycopyしたければ、こう
# >>> import copy
# >>> c=copy.deepcopy(b)
# >>> c.append(9)
# >>> print c,b
# [1, 2, 3, 8, 9] [1, 2, 3, 8]


## copyを使えばいい
# >>> a=[1,2,3]
# >>> b=copy.copy(a)
# >>> b.append(4)
# >>> print a,b
# [1, 2, 3] [1, 2, 3, 4]

## ただしlist内のlistは、、、
# >>> list_of_lists=[['a'],[1,2,],['z',23]]
# >>> copy_lol=copy.copy(list_of_lists)
# >>> copy_lol[1].append('boo')
# >>> print list_of_lists,copy_lol
# [['a'], [1, 2, 'boo'], ['z', 23]] [['a'], [1, 2, 'boo'], ['z', 23]]



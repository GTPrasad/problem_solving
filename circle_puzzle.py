# Soldiers standing in a circle, first soldier has a knife.
# He will kill the soldier next(second) to him and passes knife to third soldier, third soldier repeats same.
# Who will be alive at the end
import copy


num = list(range(1, 50))

"""1,2,3,4,5,6,7,8,9,10,11,12,13,14
1,3,5,7,9,11,13
5,9,13
13"""

"""1,2,3,4,5,6,7,8,9,10,11,12,13
3,5,7,9,11,13
7,11,
11"""


def circle(lst):
    temp = copy.deepcopy(lst)
    for i in range(0, len(lst)):
        if i % 2 == 1:
            temp.remove(lst[i])
    if len(lst) % 2 == 1:
        temp.remove(lst[0])
    lst = copy.deepcopy(temp)
    if len(temp) > 1:
        circle(lst)
    else:
        print("last man", temp)


print(circle(num))

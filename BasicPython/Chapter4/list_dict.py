#!/usr/bin/env python3


def SortTowLists(l1:list[int], l2:list[int]):
    result = []
    i = 0
    j = 0
    while(i < len(l1) and j < len(l2)):
        a = l1[i]
        b = l2[j]
        if a <= b:
            result.append(a)
            i+=1
        else:
            result.append(b)
            j+=1

    while(i < len(l1)):
        result.append( l1[i])
        i+=1

    while(j < len(l2)):
        result.append( l2[i])
        j+=1

    print(result)
    return result


def CountChar():
    s = "aabb"
    result = {}
    for c in s:
        if c in result:
            result[c]+=1
        else:
            result[c] = 1
    print(result)

if __name__ == "__main__":
    l1 = [1,3,5,6 ,199]
    l2 = [1,2,3,8]

    SortTowLists(l1 , l2)
    CountChar()


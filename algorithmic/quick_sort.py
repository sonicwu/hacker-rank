#!/bin/python

# Head ends here
def quickSort(ar):
    partition(ar)
    return

def partition(ar):
    if len(ar) <= 1:
        return ar

    first = ar[0]
    left = []
    right = []
    for i in range(1, len(ar)):
        if ar[i] < first:
            left.append(ar[i])
        else:
            right.append(ar[i])

    left = partition(left)
    left.append(first)
    left.extend(partition(right))

    print ' '.join(str(n) for n in left)
    return left

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
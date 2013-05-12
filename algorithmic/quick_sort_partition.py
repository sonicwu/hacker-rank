#!/bin/python

# Head ends here
def partition(ar):
    first = ar[0]
    left = []
    right = []
    for i in range(1, len(ar)):
        if ar[i] < first:
            left.append(ar[i])
        else:
            right.append(ar[i])

    left.append(first)
    left.extend(right)

    print ' '.join(str(n) for n in left)

    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
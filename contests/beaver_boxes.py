#!/bin/python
class Box:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width  = width

    def __str__(self):
        return "[{0}, {1}]".format(self.width, self.height)

    def reverse(self):
        #print "Reverse [{0}, {1}] => [{1}, {0}]".format(self.width, self.height)
        self.width, self.height = self.height, self.width

def stack(boxes):
    boxes = sorted(boxes, key = lambda box: box.width)
    for box in boxes:
        widths = [b.width for b in boxes]
        heights = [b.height for b in boxes]
        if box.height not in widths and widths.count(box.width) > 1:
            box.reverse()

if __name__ == "__main__":
    n = input()
    
    boxes = []
    for i in range(n):
        vector = [int(j) for j in raw_input().strip().split()]
        boxes.append(Box(vector[0], vector[1]))

    stack(boxes)
    print len(set([b.width for b in boxes]))
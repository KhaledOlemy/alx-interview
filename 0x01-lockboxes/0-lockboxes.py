#!/usr/bin/python3

def canUnlockAll(boxes):
    return singleBoxUnlocker(boxes, 0, [0])


def singleBoxUnlocker(boxes, keyToBox, unlockedBoxes=[0]):
    if len(unlockedBoxes) == len(boxes):
        return True
    if not boxes[keyToBox]:
        return False
    if (len(boxes[keyToBox]) == 1 and keyToBox == boxes[keyToBox][0]):
        return False
    for b in boxes[keyToBox]:
        if b != keyToBox:
            if b not in unlockedBoxes:
                unlockedBoxes.append(b)
                singleBoxUnlocker(boxes, b, unlockedBoxes)
    if len(unlockedBoxes) == len(boxes):
        return True
    return False

#!/usr/bin/python3
"""
Try to unlock all the boxes
"""


def canUnlockAll(boxes):
    """
    Wrapper function to call the main function.
    Args:
            boxes: array of arrays. each array insude represents a box
    Return:
            Boolean
    """
    return singleBoxUnlocker(boxes, 0, [0])


def singleBoxUnlocker(boxes, keyToBox, unlockedBoxes=[0]):
    """
    Main function to unlock all boxes
    Args:
            boxes: array of arrays. each array insude represents a box
            keyToBox: the box to unlock and use the keys inside
            unlockedBoxes: array of opened boxes keys to track completion
    Return:
            Boolean
    """
    if len(unlockedBoxes) == len(boxes):
        return True
    if not boxes[keyToBox]:
        return False
    # if (len(boxes[keyToBox]) == 1 and keyToBox == boxes[keyToBox][0]):
    #     return False
    for b in boxes[keyToBox]:
        if b != keyToBox:
            if b not in unlockedBoxes:
                unlockedBoxes.append(b)
                singleBoxUnlocker(boxes, b, unlockedBoxes)
    if len(unlockedBoxes) == len(boxes):
        return True
    return False

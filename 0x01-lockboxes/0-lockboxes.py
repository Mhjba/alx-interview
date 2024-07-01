#!/usr/bin/python3
"""canUnlockAll boxes"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    if not boxes:
        return False
    # Start with the first box
    unlcd_boxes = {0}
    # Get the initial set of keys
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlcd_boxes:
            unlcd_boxes.add(key)
            # Add new keys
            keys.update(boxes[key])
    # Check all
    return len(unlcd_boxes) == len(boxes)

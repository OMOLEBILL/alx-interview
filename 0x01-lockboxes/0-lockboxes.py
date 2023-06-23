#!/usr/bin/python3
""" we try to find the keys for the lockboxes """


def canUnlockAll(boxes):
    """@boxes are matrix with list"""
    n = len(boxes)  # number of boxes
    # initially, all boxes are locked except the first one
    unlocked = [False] * n
    unlocked[0] = True  # unlock the first box

    keys = boxes[0]  # keys in the first box

    while True:
        if all(unlocked):  # if all boxes are unlocked, return True
            return True

        if not keys:  # if there are no more keys to try, return False
            return False

        key = keys.pop(0)  # take the first key from the list

        # if the key opens a new box, unlock it and add its keys to the list
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return False  # should not reach here

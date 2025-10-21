"""Module for array rearrangement operations."""


def rearrange_array_alternate(input_arr):
    """
    Given an integer array, rearrange it such that it contains positive and
    negative numbers at alternate positions. If the array contains extra
    positive or negative numbers put them at the end of the array.
    Input: [9,-3,5,-2,-8,-6,1,3]
    Output: [9,-3,5,-2,1,-8,3,-6]
    """
    positives = []
    negatives = []

    for num in input_arr:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    # Build result by alternating
    result = []
    i = 0
    while i < len(positives) and i < len(negatives):
        result.append(positives[i])
        result.append(negatives[i])
        i += 1

    # Add remaining positives
    while i < len(positives):
        result.append(positives[i])
        i += 1

    # Add remaining negatives
    while i < len(negatives):
        result.append(negatives[i])
        i += 1

    return result


if __name__ == "__main__":
    rearrange_array_alternate([9, -3, 5, -2, -8, -6, 1, 3])

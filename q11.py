"""Module for inversion count operations."""

def count_inversions(arr):
    """
    Returns the count of inversions in the array.
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].

    Input: arr[] = [8, 4, 2, 1]
    Output: 6
    Explanation: Given array has six inversions:
    (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).
    """
    count = 0

    for i, val in enumerate(arr):
        for j in range(i + 1, len(arr)):
            if val > arr[j]:
                count += 1

    return count


if __name__ == "__main__":
    count_inversions([8, 4, 2, 1])

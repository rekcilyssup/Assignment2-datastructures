"""Module for array search operations."""


def find_closest_number(arr, number):
    """
    Given a sorted array of integers, find the value in the array
    that is closest to the given number.

    The array may contain duplicate and negative values.

    Example:
    Input:
        arr = [2, 42, 82, 122, 162, 202, 242, 282, 322, 362],
        number = 80
    Output: 82
    """
    if not arr:
        return None

    low = 0
    high = len(arr) - 1
    closest = arr[0]

    while low < high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        # Update closest if this value is closer
        if abs(mid_value - number) < abs(closest - number):
            closest = mid_value

        if mid_value < number:
            low = mid + 1
        elif mid_value > number:
            high = mid - 1
        else:
            return mid_value

    if abs(arr[low] - number) < abs(closest - number):
        closest = arr[low]

    return closest


if __name__ == "__main__":
    find_closest_number([2, 42, 82, 122, 162, 202, 242, 282, 322, 362], 80)

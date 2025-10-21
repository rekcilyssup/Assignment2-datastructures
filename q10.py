"""Module for pair sum search operations."""


def find_pair_with_sum(input_arr, target_sum):
    """
    Given a list of integers `input_arr` and a target sum `target_sum`,
    return the first pair of **distinct** elements from the list that add
    up to the target sum.

    - If multiple valid pairs exist, return the **first** such pair found
      while scanning from left to right.
    - If no such pair exists, return [-1].
    - The solution must run in O(n) time complexity.

    Examples:
    Input: input_arr = [0, -1, 2, -3, 1], target_sum = -2
    Output: [-3, 1]

    Input: input_arr = [1, -2, 1, 0, 5], target_sum = 0
    Output: [-1]
    Return the first valid pair [a, b] such that:
        a + b == target_sum
        a comes before b in the list ([a, b], not [b, a])
        a and b must be from different indices
    """
    seen = set()

    for num in input_arr:
        if (complement := target_sum - num) in seen:
            return [complement, num]
        seen.add(num)

    return [-1]


if __name__ == "__main__":
    find_pair_with_sum([0, -1, 2, -3, 1], -2)

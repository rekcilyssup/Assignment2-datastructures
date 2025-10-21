"""
Sorting algorithms: Bubble Sort, Selection Sort, and Insertion Sort.
"""

def bubble_sort(arr):
    """
    Given an array, return the number of rounds needed in bubble sort.
    """
    length = len(arr)
    rounds = 0
    array = arr[:]

    for i in range(length):
        swapped = False
        for j in range(0, length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            rounds += 1
        else:
            break

    return rounds

def selection_sort(arr):
    """
    Sort array using selection sort.
    """
    array = arr[:]
    length = len(array)

    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j

        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]

    return array

def insertion_sort(arr):
    """
    Sort array using insertion sort.
    """
    array = arr[:]
    length = len(array)

    for i in range(1, length):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


if __name__ == "__main__":
    bubble_sort([64, 34, 25, 12, 22, 11, 90])
    selection_sort([64, 25, 12, 22, 11])
    insertion_sort([12, 11, 13, 5, 6])

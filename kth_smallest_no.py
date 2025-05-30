# -*- coding: utf-8 -*-
"""Kth_smallest_no.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1APEi3JjXyD5UfGx2BeSGl5JqHy0A4AfX
"""

import random

# Helper function to partition the array
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized Partition
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with the last element
    return partition(arr, low, high)

# Randomized Quickselect
def randomized_quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = randomized_partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return randomized_quickselect(arr, pivot_index + 1, high, k)
        else:
            return randomized_quickselect(arr, low, pivot_index - 1, k)

# Example Usage
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3  # Find the 3rd smallest number (k is zero-based)
result = randomized_quickselect(arr, 0, len(arr) - 1, k - 1)
print(f"The {k}-th smallest element is: {result}")


import time
import random

# -------------------------------
# Deterministic QuickSort
# -------------------------------
def deterministic_quicksort(arr):
    """Performs deterministic QuickSort (pivot = last element)."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # Deterministic pivot: last element
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

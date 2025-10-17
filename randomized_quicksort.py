# -------------------------------
# Randomized QuickSort
# -------------------------------
def randomized_quicksort(arr):
    """Performs Randomized QuickSort (pivot chosen randomly)."""
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Builds the sorted list one element at a time by inserting each into its place.
    O(n²) time, in-place, stable.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr):
    """
    Generalization of insertion sort that starts by sorting distant elements.
    Uses gap sequence: n//2, n//4, …, 1.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort(arr):
    """
    Divide-and-conquer: split in halves, sort each, and merge.
    O(n log n) time, O(n) extra space, stable.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr):
    """
    In-place QuickSort using Lomuto partition. Average O(n log n), worst O(n²).
    """
    def _qs(a, low, high):
        if low < high:
            p = partition(a, low, high)
            _qs(a, low, p - 1)
            _qs(a, p + 1, high)

    def partition(a, low, high):
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    _qs(arr, 0, len(arr) - 1)
    return arr

def heap_sort(arr):
    """
    Builds a max-heap then extracts the max to the end repeatedly.
    O(n log n) time, in-place.
    """
    def heapify(a, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(a, n, largest)

    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def radix_sort(arr):
    """
    Least Significant Digit (LSD) Radix Sort for non-negative integers.
    O(d·(n + k)) time, where d = #digits, k = base (10).
    """
    if not arr:
        return arr
    # Ensure all non-negative
    assert all(isinstance(x, int) and x >= 0 for x in arr), "LSD Radix only for non-negative ints"
    max_val = max(arr)
    exp = 1
    n = len(arr)
    output = [0] * n

    while max_val // exp > 0:
        count = [0] * 10
        # Count occurrences
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1
        # Prefix sums
        for i in range(1, 10):
            count[i] += count[i - 1]
        # Build output array (stable)
        for num in reversed(arr):
            idx = (num // exp) % 10
            output[count[idx] - 1] = num
            count[idx] -= 1
        # Copy back
        arr[:] = output[:]
        exp *= 10

    return arr

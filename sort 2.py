# The Merge function: Combines two sorted halves
def merge(arr, left, mid, right):
    temp = []
    i = left       # Pointer for Left half
    j = mid + 1    # Pointer for Right half

    # Compare and merge
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Cleanup remaining elements in Left half (if any)
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Cleanup remaining elements in Right half (if any)
    while j <= right:
        temp.append(arr[j])
        j += 1

    # Copy the merged temp array back into the original array
    for k in range(left, right + 1):
        arr[k] = temp[k - left]

# The recursive Divide function
def merge_sort(arr, left, right):
    if left >= right: return # Base case: 1 element is already sorted

    mid = left + (right - left) // 2

    merge_sort(arr, left, mid)      # Sort Left half
    merge_sort(arr, mid + 1, right) # Sort Right half
    merge(arr, left, mid, right)    # Merge them together
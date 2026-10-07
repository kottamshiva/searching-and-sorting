def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Condition 1: Left half is sorted
        if nums[left] <= nums[mid]:
            # Is the target inside this sorted box?
            if nums[left] <= target < nums[mid]:
                right = mid - 1 # Yes, discard right half
            else:
                left = mid + 1  # No, discard left half

        # Condition 2: Right half is sorted
        else:
            # Is the target inside this sorted box?
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Yes, discard left half
            else:
                right = mid - 1 # No, discard right half

    return -1 # Target not found
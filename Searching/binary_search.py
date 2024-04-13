def BinarySearch(nums, left, right, target):
	if right >= left:
		midd_idx = (left + right) // 2
	
		if nums[midd_idx] == target:
			return target
		elif nums[midd_idx] < target:
			return BinarySearch(nums, midd_idx+1, right, target)
		elif nums[midd_idx] > target:
			return BinarySearch(nums, left, midd_idx-1, target)
	
		else:
			return -1
	
nums = [1,2,3,4,5,6]

result = BinarySearch(nums, 0, len(nums), 2)

print(result)
		
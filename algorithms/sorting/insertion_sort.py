def insertion_sort(nums):
	for n in range(1, len(nums)):
		while nums[n] < nums[n - 1] and n > 0:
			temp = nums[n]
			nums[n] = nums[n - 1]
			nums[n - 1] = temp
			n -= 1

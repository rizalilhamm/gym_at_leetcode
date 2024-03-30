class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[zeroIdx] = nums[idx]
                zeroIdx += 1

        while zeroIdx != len(nums):
            nums[zeroIdx] = 0
            zeroIdx += 1
        
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         last_non_zero_idx = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[last_non_zero_idx], nums[i] = nums[i], nums[last_non_zero_idx]
#                 last_non_zero_idx += 1
#             print('nums: ', nums)
           
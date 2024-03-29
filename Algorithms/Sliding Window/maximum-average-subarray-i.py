class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        i = 0
        avg = nums[0]
        for i in range(1, k):
            avg += nums[i]

        max = avg / k

        for j in range(k, len(nums)):
            avg += nums[j]
            avg -= nums[j-k]

            max = max if max > avg / k else avg / k

        return max

            
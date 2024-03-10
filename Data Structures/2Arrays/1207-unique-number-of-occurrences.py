# Problem Link: https://leetcode.com/problems/unique-number-of-occurrences

class Solution(object):
    def uniqueOccurrences(self, nums):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False

        hashMap = {}
        temps = []

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key in hashMap.keys():
            if hashMap[key] in temps:
                return False
            else:
                temps.append(hashMap[key])
    
        return True
            
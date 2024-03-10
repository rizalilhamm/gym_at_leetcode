class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        resp = []
        looped = nums1 if len(nums1) < len(nums2) else nums2

        for num in looped:
            if num in nums1 and num in nums2 and num not in resp:
                resp.append(num)
        
        return resp
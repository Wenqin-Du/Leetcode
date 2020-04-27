
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = {}
        res = []
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        for num in nums2:
            if num in count1 and count1[num] > 0:
                res. append(num)
                count1[num] -= 1
        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()

        for num in nums:
            # combine if&else in one line
            counts[num] = counts.get(num, 0) + 1
        print(counts)

        for k, v in counts.items():
            if v > (len(nums) // 2):
                return(k)

        # quick way
        # return sorted(nums)[len(nums)//2]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            else:
                digits[~i] = 0

        return [1] + [0] * len(digits)


        # nums = ''.join(str(i) for i in digits)
        # nums = 1 + int(nums)
        # nums = str(nums)
        # result = []
        # for i in range(len(nums)):
        #     result.append(nums[i])
        # return result




def plusOne(digits):

    for i in range(len(digits)):
        if digits[~i] < 9:
            print(i)
            print(digits[~i])
            digits[~i] += 1
            return digits
        else:
            digits[~i] = 0

    return [1] + [0] * len(digits)


plusOne([9,9,9,9,9,9])

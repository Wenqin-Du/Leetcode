
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        l, r = 0, len(letters)-1
        while l < r:
            mid = (l+ r) // 2
            if target < letters[mid]:
                r = mid
            else:
                l = mid + 1
        return letters[l]




class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k # l,r for start point.  len(arr) - k: max start point

        while l < r:
            mid = (l + r) // 2

            # "mid + k is closer to x"
            # not use abs() for duplicate numbers
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                r = mid
        return arr[l : l + k]



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i: i + len(neddle)] == neddle:
                return i
            i += 1

        return -1


a = "hello"
print(a[2:4])

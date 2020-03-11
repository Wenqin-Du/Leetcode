
class Solution:
    def lengthOfLongestSubstring(self, s):

        used = {}
        start = max_length = 0

        for i,v in enumerate(s):
            if v in used and used[v] >= start:
                start = used[v] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[v] = i

        return max_length


# check

def lengthOfLongestSubstring(s):

    used = {}
    start = max_length = 0

    for i,v in enumerate(s):
        if v in used and used[v] >= start:
            start = used[v] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[v] = i

    return max_length


print(lengthOfLongestSubstring("abcccdefgh"))


# review enumerate

nums = "abbb"
for i,v in enumerate(nums):
    print(i, v)

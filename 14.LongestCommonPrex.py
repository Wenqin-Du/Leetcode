
class Solution:
    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str];
        rtype: str
        """

        sepInOrder, pref = list(zip(*strs)), ""

        for word in sepInOrder:
            if len(set(word)) == 1:
                pref += word[0]
            else:
                break

        return pref



# 自我检查及函数补充

a = "asdf"
print(list(zip(*a)))
print(list(zip(a)))

strs = ["flower","flow","flight"]
print(list(zip(*strs)))

a = ["asdf"]
print(list(zip(*a)))

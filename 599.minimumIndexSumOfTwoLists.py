
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        if len(list1) < len(list2):
            dic, dic2 = {v : i for i, v in enumerate(list1)}, {}
            for i, v in enumerate(list2):
                if v in dic:
                    dic2[v] = dic.get(v) + i
            return [key for key in dic2 if dic2[key] == min(dic2.values())]
        else:
            dic, dic2 = {v : i for i, v in enumerate(list2)}, {}
            for i, v in enumerate(list1):
                if v in dic:
                    dic2[v] = dic.get(v) + i
            return [key for key in dic2 if dic2[key] == min(dic2.values())]



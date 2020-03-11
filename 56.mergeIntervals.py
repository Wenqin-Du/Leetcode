
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        orderintervals = sorted(intervals)
        result = []

        for i in range(len(intervals)):
            if result and result[-1][1] >= orderintervals[i][0]:
                result[-1] = [result[-1][0], max(orderintervals[i][1], result[-1][1])]
                #  改进 result[-1][-1] = max(orderintervals[i][1], result[-1][1])

            else:
                result += [orderintervals[i]]

        return result

        # 以下为更快的写function的方法
        # out = []
        # for i in sorted(intervals, key=lambda i: i[0]):
        #     if out and i[0]<=out[-1][-1]:
        #         out[-1][-1] = max(out[-1][-1], i[-1])
        #     else: out+=[i]
        # return out



def merge(intervals):

        orderintervals = sorted(intervals)
        result = []

        for i in range(len(intervals)):
            if result and result[-1][1] >= orderintervals[i][0]:
                result[-1] = [result[-1][0], max(orderintervals[i][1], result[-1][1])]

            else:
                result += [orderintervals[i]]

        return result



intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
merge(intervals)

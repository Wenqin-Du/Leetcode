
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '':
            return []

        worddic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mon', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        from functools import reduce

        return reduce(lambda acc, num: [x + y for x in acc for y in worddic[num]], digits, [''])

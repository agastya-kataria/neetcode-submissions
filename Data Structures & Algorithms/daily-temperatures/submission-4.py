class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, x in enumerate(temperatures):
            while stack and stack[-1][0]<x:
                stackT, stackI = stack.pop()
                res[stackI] = (i-stackI)
            
            stack.append((x, i))
        return res
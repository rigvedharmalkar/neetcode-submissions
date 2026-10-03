class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {")":"(","]":"[","}":"{"}
        stack = []

        for w in s:
            if w in closeToOpen:
                if stack and stack[-1] == closeToOpen[w]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(w)

        return True if not stack else False
            



        
        

        
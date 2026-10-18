class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s]for p,s in zip(position, speed)] # this is an array of pairs 
        pair.sort(reverse=True) # we are starting with the left side 
        stack=[]
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack [-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        
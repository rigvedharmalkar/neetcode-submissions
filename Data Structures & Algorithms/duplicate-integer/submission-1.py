class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictt = {}

        for num in nums:
            if num not in dictt:
                dictt[num] = 1
            else:
                dictt[num] += 1
        
        for k,v in dictt.items():
            if v > 1:
                return True
        return False
 
        

        
            
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comp = 0
        dictt = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in dictt:
                return [dictt[comp],i]
            else:
                dictt[nums[i]] = i
            
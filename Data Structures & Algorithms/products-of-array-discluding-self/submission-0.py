class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []

        for i in range(len(nums)):
            arr = nums.copy()
            arr.pop(i)
            mul = 1
            for i in range(len(arr)):
                mul *= arr[i]
            res.append(mul)
        return res



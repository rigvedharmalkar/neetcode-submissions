class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_count = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                val = nums[i]
                count = 1
                while val + 1 in nums:
                    count += 1
                    val += 1
                max_count = max(count,max_count)
        return max_count
        
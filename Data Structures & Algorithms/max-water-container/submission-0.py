class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        max_area = 0

        while left < right:

            length = min(nums[left],nums[right])
            area = length * (right - left)

            max_area = max(area,max_area)

            if nums[left] > nums[right]:
                right -= 1
            else:
                left += 1
        return max_area
        
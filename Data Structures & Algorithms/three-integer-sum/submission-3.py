class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using two sum approach
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            left, right = i+1, n-1
            curr = nums[i]
            if curr > 0:
                return result
            # watch out for duplicate values
            if i > 0 and curr == nums[i-1]:
                continue
            while left < right:
                three_sum = curr + nums[left] + nums[right]
                if three_sum == 0:
                    result.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # watch out for duplicate values here!
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
            
        return result
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. sort -> two pointer: time O(nlogn), space O(1) but this array is already sorted!
        # 2. put in a set and iterate the array: time O(N), extra space O(N)
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

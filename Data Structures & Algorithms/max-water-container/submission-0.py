class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        max_water = 0
        while left < right:
            max_water = max(max_water, (right-left) * min(heights[left], heights[right]))
            # question for when heights[left] == heights[right]
            # 둘이 같으면 어느 한쪽을 움직여도 최대 높이는 항상 heights[left or right]이고, width는 -1이 되므로 어느 쪽을 움직여도 상관이 없다.
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return max_water
                
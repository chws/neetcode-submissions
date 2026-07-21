class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1) use division, 2) multiply left/right
        # save products from the left
        # 1, 2, 4, 6
        # 1, 2, 8, 48
        n = len(nums)
        left_products = [0] * n
        for i, num in enumerate(nums):
            if i == 0:
                left_products[i] = num
            else:
                left_products[i] = left_products[i-1] * num
                
        # save products from the right
        # 48, 48, 24, 6
        right_products = [0] * n
        for i in range(n):
            actual_idx = n - 1 - i
            if i == 0:
                right_products[actual_idx] = nums[actual_idx]
            else:
                right_products[actual_idx] = right_products[actual_idx+1] * nums[actual_idx]
    
        # multiply left[i-1] * right[i+1]
        left_products = [1] + left_products + [1]
        right_products = [1] + right_products + [1]
        result = [0] * n
        for i in range(1, n+1):
            result[i-1] = left_products[i-1] * right_products[i+1]
        return result
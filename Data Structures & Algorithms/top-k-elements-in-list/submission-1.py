class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. sort, 2. heap, 3. bucket

        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for key, val in count.items():
            bucket[val].append(key)
        
        top_k_freq = []
        for lst in bucket[::-1]:
            top_k_freq += lst
            if len(top_k_freq) == k:
                return top_k_freq
        return null
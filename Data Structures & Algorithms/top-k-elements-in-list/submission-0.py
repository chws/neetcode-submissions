class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurences
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # format: [count: number of occurences]
        count_list = [(-val, key) for key, val in count.items()]

        heapq.heapify(count_list)
        top_k_freq = []
        for _ in range(k):
            val, key = heapq.heappop(count_list)
            top_k_freq.append(key)
        
        return top_k_freq
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k most frequent.
        # have a min heap
        # from there, keep track of the frequencies and if the current
        # frequency is greater than the min frequency, then pop the head
        # and push

        frequency = {} # num: frequency[int]
        min_heap = []

        # maybe build frequency table separately?
        # O(n)

        # Runtime is O(nlogk).
        # We do heappush and heappop (Which is logk) and then we do this
        # at most n times since the for loop runs n times.

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1  

        for num in frequency:
            freq = frequency[num]
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, num))

        return [num[1] for num in min_heap]


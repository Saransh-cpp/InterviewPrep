import heapq

def topKFrequent(nums, k):
    freq = {}
    for num in nums:       
        freq[num] = freq.get(num, 0) + 1
    h = [(v, k) for k, v in freq.items()]
    heapq.heapify(h)
    return [x[1] for x in heapq.nlargest(k, h)]

import heapq

def findKthLargest(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for num in nums[k:]:
        if num >= h[0]:
            heapq.heappushpop(h, num) 
    return h[0]

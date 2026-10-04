def maxArea(height):
    high = len(height) - 1
    low = 0
    max_water = 0
    while low < high:
        if height[low] < height[high]:
            max_water = max(max_water, height[low] * (high - low))
            low += 1
        else:
            max_water = max(max_water, height[high] * (high - low))
            high -= 1
    return max_water

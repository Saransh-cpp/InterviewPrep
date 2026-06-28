def trap(height):
    left_max = [-1]
    right_max = [-1]

    for i in range(1, len(height)):
        left_max.append(max(height[i - 1], left_max[-1]))
    for i in range(len(height) - 2, -1, -1):
        right_max.append(max(height[i + 1], right_max[-1]))
    right_max.reverse()

    water = 0
    for i in range(len(height)):
        if left_max[i] > height[i] and right_max[i] > height[i]:
            water += min(left_max[i], right_max[i]) - height[i]
    return water

def trap(height):
    left_max = height[0]
    right_max = height[-1]
    left = 0
    right = len(height) - 1
    water = 0
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(height[left], left_max)
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(height[right], right_max)
            water += right_max - height[right]
    return water

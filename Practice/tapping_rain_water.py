height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap(height):
    if not height:
        return 0

    volumn = 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 더 높은 쪽으로 포인터 이동
        if left_max <= right_max:
            volumn += left_max - height[left]
            left += 1
        else:
            volumn += right_max - height[right]
            right -= 1
        return volumn


print(trap(height))
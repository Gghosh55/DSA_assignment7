def isStrobogrammatic(num):
    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] + num[right] not in ["00", "11", "69", "96", "88"]:
            return False
        left += 1
        right -= 1

    return True
num = "69"
print(isStrobogrammatic(num))

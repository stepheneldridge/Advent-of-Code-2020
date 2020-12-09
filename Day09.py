INPUT = open("Day09.txt", 'r')
nums = []
for line in INPUT:
    nums.append(int(line.strip()))

pre = 25

def check_sums(index):
    goal = nums[index]
    for i in range(pre):
        for j in range(i + 1, pre):
            if nums[index + i - pre] + nums[index + j - pre] == goal:
                return True
    return False

index = pre
while index < len(nums):
    if not check_sums(index):
        goal = nums[index]
        break
    index += 1
print("part 1:", goal)

def find_subsum():
    start = 0
    while start < len(nums):
        subsum = nums[start]
        for i in range(start + 1, len(nums)):
            subsum += nums[i]
            if subsum == goal:
                sub = nums[start:i + 1]
                return min(sub) + max(sub)
            elif subsum > goal:
                break
        start += 1

print("part 2:", find_subsum())
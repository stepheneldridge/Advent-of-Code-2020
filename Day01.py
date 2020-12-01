INPUT = open("Day01.txt", 'r')
nums = []
for i in INPUT:
    try:
        x = int(i)
        nums.append(x)
    except:
        pass

def get():
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[i] + nums[i + j + 1] == 2020:
                return nums[i] * nums[i + j + 1]

print("part 1:", get())

def getter():
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            for k in range(len(nums) - i - j - 2):
                if nums[i] + nums[i + j + 1] + nums[i + j + k + 2] == 2020:
                    return nums[i] * nums[i + j + 1] * nums[i + j + k + 2]

print("part 2:", getter())
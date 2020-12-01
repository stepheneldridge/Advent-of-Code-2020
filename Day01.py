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
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]

print("part 1:", get())

def getter():
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            for k in range(len(nums) - i - j - 1):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]

print("part 2:", getter())
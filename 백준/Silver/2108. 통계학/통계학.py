def frequency(nums):
    dictNums = {}
    for num in nums:
        if num not in dictNums:
            dictNums[num] = 1
        else:
            dictNums[num] += 1

    maxDictNums = max(dictNums.values())
    countingList = []

    for value in dictNums:
        if dictNums[value] == maxDictNums:
            countingList.append(value)

    if len(countingList) > 1:                   # 최빈값이 여러 개인 경우
        print(countingList[1])
    else:                                       # 최빈값이 하나인 경우
        print(countingList[0])

N = int(input())
nums = [int(input()) for _ in range(N)]

print(round(sum(nums) / N))           # 산술 평균

nums.sort()         
print(nums[N // 2])             # 중앙값

frequency(nums)                 # 최빈값

print(max(nums) - min(nums))    # 범위
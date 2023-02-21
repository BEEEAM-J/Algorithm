def frequency(nums):                            # 최빈값 구하는 함수
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

print(round(sum(nums) / N))     # 산술 평균
nums.sort()         
print(nums[N // 2])             # 중앙값
frequency(nums)                 # 최빈값
print(max(nums) - min(nums))    # 범위

# 숫자들을 입력 받아서 이의 산술 평균, 중앙갑스 최빈값, 범위를 구하는 문제이다.
# 산술 평균, 중앙값, 범위는 간단한 연산으로 출력을 하였다.
# 최빈값은 숫자들 중 가장 많이 나타나는 값을 찾는데 여러 개가 있는 경우에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 키가 숫자이고, 값이 빈도인 딕셔너리를 만들고, 빈도 값중 최대 값을 찾는다. 
# 그리고 방금 찾은 최대 값을 딕셔너리의 값(빈도)들과 비교를 해서 같으면 다른 리스트에 추가를 했다.
# 마지막으로 리스트의 길이가 1보다 크면(최빈값이 여러 개인 경우) 해당 리스트의 두 번째 값을 출력하고, 
# 아닌 경우(최빈값이 하나인 경우) 해당 리스트의 첫 번째 값을 출력하게 하였다. 

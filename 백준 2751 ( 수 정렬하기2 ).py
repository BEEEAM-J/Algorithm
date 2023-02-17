N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()
for num in nums:
    print(num)

# 그냥 입력 받아서 sort로 정렬하고 순서대로 출력하면 끝!
# pypy3로 돌려야지 백준에서 시간초과가 안나옴

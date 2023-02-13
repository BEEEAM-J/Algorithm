def binary_search(target, data):

    start = 0                           # 범위의 첫 번째 값
    end = len(data) - 1                 # 범위의 마지막 값

    while start <= end:     
        mid = (start + end) // 2        # 범위의 중간 값(이 값을 target과 비교하면서 범위를 좁힌다.)

        if data[mid] == target:         # 값을 찾은 경우
            print(1)
            return 0
        elif data[mid] > target:        # 범위의 중간 값이 목표 값보다 큰 경우
            end = mid - 1               # 범위의 끝을 중간 - 1로 좁힌다.
        else:                           # 범위의 중간 값이 목표 값보다 작은 경우
            start = mid + 1             # 범위의 시작을 중간 + 1로 좁힌다.
    print(0)

N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))
NList.sort()

for i in MList:
    binary_search(i, NList)

# 처음 입력 받은 리스트의 수들이 나중에 입력 받은 리스트 안에 있는지 확인하는 문제이다.
# 2중 for문을 돌려서 각 요소에 대해서 있는지 확인을 하는 방법을 사용하면 시간 초과가 발생한다.
# 그래서 이분 탐색을 사용해야 한다. 
# 모든 수에 대해서 검사하는게 아니라 범위를 정해서 목표값에 따라서 범위를 좁히면서 탐색을 하기 때문에 더 빨리 탐색이 가능하다.

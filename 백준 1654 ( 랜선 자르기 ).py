def binary_search(N, lens):
    start, end = 1, max(lens)
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        # 자르고, 개수를 계산하는 부분
        for len in lens:
            cnt += len // mid

        # 개수를 가지고 이분 탐색을 하는 부분
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

K, N = map(int, input().split())
lanLens = []
for _ in range(K):
    lanLens.append(int(input()))
binary_search(N, lanLens)

# K개의 랜선들이 주어지고, 이 랜선들을 잘라서 N개로 만드는데 이때 만들수 있는 최대 랜선의 길이를 구하는 문제이다.
# start 값은 1, end 값은 주어진 랜선들 중 가장 긴 길이로 설정한다. 
# 그리고 범위의 중간 값으로 랜선들을 자르고 길이를 구한다. 
# 다음 계산 된 값을 N과 비교하여 범위를 좁힌다. 
# 이러한 과정을 이분 탐색으로 계속 진행하면 답이 나온다.  

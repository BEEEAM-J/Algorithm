def binary_search(trees):
    start, end = 1, max(trees)

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for i in trees:                     # 나무들을 자르는 과정
            if mid <= i:                    # 자를 수 있는 나무이면 자른다.
                total += i - mid

        if total >= M:                      # 자른 나무들의 합으로 이분탐색하여 범위 조정
            start = mid + 1
        else:
            end = mid - 1
    print(end)    

N, M = map(int, input().split())
trees = list(map(int, input().split()))
binary_search(trees)

# N개의 나무들을 한번에 잘라서 M에 가까운 값이 나오게 하는 높이를 찾아야 한다.
# 자를 높이는 이분 탐색으로 찾아야 한다.
# 먼저 1부터 나무들의 가장 긴 값의 중간 값으로 나무를 자르고, 나무들의 합과 M을 비교해서 범위를 좁혀간다.  

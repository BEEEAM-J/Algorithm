from itertools import permutations

cases = list(permutations([1,2,3,4,5,6,7,8,9], 3))      # 답이 될 수 있는 모든 경우를 생성

N = int(input())
for _ in range(N):
    inputNums, strike, ball = map(int, input().split())
    inputNums = list(str(inputNums))
    removeCnt = 0

    for i in range(len(cases)):
        strikeCnt, ballCnt = 0, 0
        i -= removeCnt
        
        for j in range(3):                                      
            if int(inputNums[j]) in cases[i]:           # 만약 입력 받은 값의 개별 요소가 비교하는 경우의 수에 들어있다면? 
                if int(inputNums[j]) == cases[i][j]:    # 위치가 같으면 스트라이크
                    strikeCnt += 1
                else:                                   # 위치가 다르므로 볼
                    ballCnt += 1
            
        if strikeCnt != strike or ballCnt != ball:      # 스트라이크나 볼의 개수가 입력 받은 스트라이크, 볼 개수와 다르다면 답이 될 수 없으므로 제거한다.
            del cases[i]
            removeCnt += 1

print(len(cases))    

# 먼저 답이 될 수 있는 모든 경우를 생성한다.
# 그리고 입력값을 모든 경우들과 비교를 해서 스트라이크, 볼 개수가 다른 경우는 모두 제거하였다.
# 그러면 마지막에는 답이 될 수 있는 경우들만 남게 된다.

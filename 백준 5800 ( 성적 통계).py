K = int(input())

grades = []
difference = []

for i in range(K):
    input_data = input().split()
    N = int(input_data[0])

    print("Class {}".format(i + 1))
    
    for j in range(N):
        grades.append(int(input_data[j + 1]))
    
#   성적을 내림차순으로 정렬    
    grades.sort(reverse=True)

#   가장 큰 인접한 점수 차이 구하기
    for h in range(len(grades) - 1):
        difference.append(grades[h] - grades[h + 1])
    
    print("Max {}, Min {}, Largest gap {}".format(max(grades), min(grades), max(difference)))
    grades.clear()
    difference.clear()

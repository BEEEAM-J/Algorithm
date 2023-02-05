heights = []
for _ in range(9):
    heights.append(int(input()))

sumHeights = sum(heights)

for i in range(8):
    for j in range(i + 1, 9):                   # 범위가 i + 1부터 9까지인 이유는 중복되는 인덱스를 확인하는 경우를 없애기 위해서이다.
        if (sumHeights - heights[i] - heights[j]) == 100:
            del heights[i]
            del heights[j - 1]                  # index가 j - 1이 되는 이유는 위에서 요소를 1개 제거 했기 때문이다.
            heights.sort()

            for k in heights:
                print(k)
            exit()

# 9개의 수 중에서 2개의 수를 제거해서 합이 100이 되게 해야된다.
# 2중 for문을 돌려서 2개의 수를 뺐을 때 100이 되는지 확인을 한다.
# 문제에서 가능한 경우가 여러 개이면 아무거나 출력해도 된다고 했다. 
# 그래서 위의 조건을 만족하면 해당하는 인덱스의 값들을 제거하고 출력을 하게 했다.

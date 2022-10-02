N, K = map(int, input().split())

coins = []
cnt = 0

for i in range(N):
    coins.append(int(input()))

j = len(coins)

while K != 0:
# 동전으로 총액을 만들수 있는 동전 개수
    cnt += K // coins[j - 1]
# 동전으로 환산된 액수를 뺀 나머지를 또 동전으로 바꿔야 함
    K %= coins[j - 1]
    j -= 1

print(cnt)

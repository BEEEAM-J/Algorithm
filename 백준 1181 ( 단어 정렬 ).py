N = int(input())

words = [input() for _ in range(N)]
words = set(words)                      # 중복 단어 제거
words = list(words)                     
words.sort()                            # 사전 순으로 정렬
words.sort(key=len)                     # 길이 순으로 정렬

for word in words:
    print(word)

# 단어를 조건에 맞게 정렬하는 문제이다.
# 조건 1. 길이가 짧은 것부터
# 조건 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.
# sort() 함수를 사용하면 쉽게 풀 수 있는 문제이다.
# 먼저 중복되는 단어를 하나만 남기기 위해서 set으로 바꿨다가 다시 리스트로 바꿨다.
# 다음 sort() 함수를 두 번 사용하는데 먼저 인자 없이 sort() 함수를 사용하여 단어들을 사전 순으로 정렬 하였다.
# 그리고 sort() 함수에 key 값으로 len을 전달하여 단어들을 길이 순으로 정렬하면 끝이다.

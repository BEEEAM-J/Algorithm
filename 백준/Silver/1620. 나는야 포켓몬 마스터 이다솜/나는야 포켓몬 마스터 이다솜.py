n, m = map(int, input().split())

pokemonKeyValue = {}
pokemonValueKey = {}

for index in range(1, n + 1):
    pokemonName = input()
    pokemonKeyValue[index] = pokemonName
    pokemonValueKey[pokemonName] = index

for _ in range(m):
    question = input()
    if question.isdigit() == True:      #  input 값이 숫자인 경우 상황
        print(pokemonKeyValue[int(question)])
    else:
        print(pokemonValueKey.get(question))
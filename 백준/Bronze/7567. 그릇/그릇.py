st = input()
total = 10
for i in range(len(st) - 1):
    if st[i] != st[i + 1]:
        total += 10
    elif st[i] == st[i + 1]:
        total += 5
print(total)
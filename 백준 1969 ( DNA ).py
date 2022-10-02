N, M = map(int, input().split())
res = 0

list_t = []
DNAs = []
nucleotide = []
nu_n = [0] * 4

for i in range(N):
    DNAs.append(input())

for j in range(M):   
    for i in range(N):
        list_t.append(DNAs[i][j])

# DNA의 요소에서 각 알파벳의 개수를 추출하여 리스트에 추가한다.
# ex) [A의 개수, C의 개수, G의 개수, T의 개수]
        if DNAs[i][j] == "A":
            nu_n[0] += 1
        elif DNAs[i][j] == "C":
            nu_n[1] += 1
        elif DNAs[i][j] == "G":
            nu_n[2] += 1        
        elif DNAs[i][j] == "T":
            nu_n[3] += 1

# 가장 많은 알파벳이 무엇인지 알아내는 과정,
# 전체 DNA 개수 - 가장 많은 알파벳의 개수 = Hamming Distance 합
    if nu_n.index(max(nu_n)) == 0:
        nucleotide.append("A")
        res += N - max(nu_n)
    elif nu_n.index(max(nu_n)) == 1:
        nucleotide.append("C")
        res += N - max(nu_n) 
    elif nu_n.index(max(nu_n)) == 2:
        nucleotide.append("G")
        res += N - max(nu_n)       
    elif nu_n.index(max(nu_n)) == 3:
        nucleotide.append("T")
        res += N - max(nu_n)
      
    nu_n = [0] * 4

print("".join(s for s in nucleotide))
print(res)

        
# 풀이
# 모든 DNA들의 각 위치들을 비교를 한다. 
# 세로로 비교를 해서 같은게 가장 많은 것을 추려서 문자열로 만들면 Hamming Distance이 가장 작은 DNA가 만들어진다.
# 그리고 세로로 비교하였을 때 다른 것들의 숫자를 다 더하면 Hamming Distance의 합이 나온다.

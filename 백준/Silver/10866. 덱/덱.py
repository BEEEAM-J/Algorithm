from collections import deque
import sys

d = deque()
N = int(input())

for i in range(0, N):
    inputStr = sys.stdin.readline().split()
    if(inputStr[0] == "push_front"): 
        d.appendleft(inputStr[1])
    elif(inputStr[0] == "push_back"): 
        d.append(inputStr[1])
    elif(inputStr[0] == "pop_front"): 
        if(len(d) == 0):
            print(-1)
        else:
            print(d.popleft())
    elif(inputStr[0] == "pop_back"): 
        if(len(d) == 0):
            print(-1)
        else:
            print(d.pop())
    elif(inputStr[0] == "size"): 
        print(len(d))
    elif(inputStr[0] == "empty"): 
        if(len(d) == 0):
            print(1)
        else:
            print(0)
    elif(inputStr[0] == "front"): 
        if(len(d) == 0):
            print(-1)
        else:
            print(d[0])
    elif(inputStr[0] == "back"): 
        if(len(d) == 0):
            print(-1)
        else:
            print(d[len(d) - 1])
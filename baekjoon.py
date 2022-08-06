def dfs(graph, start, visited = []):
    visited.append(start)                   # 방문 처리
    # print(visited)                          # 추가되는 순서 보여줌

    for node in graph[start]:               # 인접 노드 확인
        if node not in visited:             # 인접 노드들 중에서 방문하지 않은것 찾기
            dfs(graph, node, visited)
            
    return visited
    

graph = dict()                      
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))
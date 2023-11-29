import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        List<Integer> visitedNode = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        Map<Integer, List<Integer>> graph = new HashMap<>();

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());

            if(graph.containsKey(first)) {
                graph.get(first).add(second);   // 이미 등록 되어 있는 노드이면 value에 값 추가
            }
            else {
                List<Integer> initList = new ArrayList<>();
                initList.add(second);
                graph.put(first, initList);     // 처음 보는 노드이면 그래프에 등록
            }

            if(graph.containsKey(second)) {
                graph.get(second).add(first);   // 이미 등록 되어 있는 노드이면 value에 값 추가
            }
            else {
                List<Integer> initList = new ArrayList<>();
                initList.add(first);
                graph.put(second, initList);     // 처음 보는 노드이면 그래프에 등록
            }
        }

        dfs(graph, V, visitedNode);

        for(int node: visitedNode) {
            System.out.print(node + " ");
        }
        visitedNode.clear();
        System.out.println();

        bfs(graph, V, visitedNode, queue);
        for(int node: visitedNode) {
            System.out.print(node + " ");
        }
    }

    static void dfs(Map<Integer, List<Integer>> graph, int start, List<Integer> visited) {
        if(!visited.contains(start)) {       // 방문한 노드인지 확인 (방문 안한 노드를 방문하고 방문 처리할 예정)
             visited.add(start);

             if(graph.get(start) != null) {
                 for(int j = 0; j < graph.get(start).size(); j++) {          // 해당 노드의 자식 노드들 검사
                     Collections.sort(graph.get(start));
                     if(!visited.contains(graph.get(start).get(j))) {        // 이미 방문한 노드인지 확인 (방문 안했으면 방문)
                         dfs(graph, graph.get(start).get(j), visited);       // 방문
                     }
                 }
             }
        }
    }

    static void bfs(Map<Integer, List<Integer>> graph, int start, List<Integer> visited, Queue<Integer> queue) {
        if(!visited.contains(start)) {       // 방문한 노드인지 확인 (방문 안한 노드를 방문하고 방문 처리할 예정)
            visited.add(start);

            if(graph.get(start) != null) {
                for(int j = 0; j < graph.get(start).size(); j++) {          // 해당 노드의 자식 노드들 검사
                    if(!visited.contains(graph.get(start).get(j))) {        // 이미 방문한 노드인지 확인 (방문 안했으면 방문)
                        if(!queue.contains(graph.get(start).get(j))) {
                            queue.add(graph.get(start).get(j));
                        }
                    }
                }
            }
            if(!queue.isEmpty()) {
                bfs(graph, queue.poll(), visited, queue);
            }
        }
    }
}
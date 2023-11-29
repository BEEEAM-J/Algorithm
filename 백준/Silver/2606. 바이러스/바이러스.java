import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int com = Integer.parseInt(br.readLine());
        int connected = Integer.parseInt(br.readLine());
        int i;
        int cnt = 0;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Boolean[] visited = new Boolean[com];

        Arrays.fill(visited, false);

        for(i = 0; i < connected; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());

            if(graph.containsKey(first)) {
                graph.get(first).add(second);
            }
            else {
                List<Integer> initList = new ArrayList<>();
                initList.add(second);
                graph.put(first, initList);
            }

            if(graph.containsKey(second)) {
                graph.get(second).add(first);
            }
            else {
                List<Integer> initList = new ArrayList<>(first);
                initList.add(first);
                graph.put(second, initList);
            }
        }
        dfs(graph, 1, visited);

        for(Boolean res: visited) {
            if(res) {
                cnt ++;
            }
        }
        System.out.print(cnt - 1);
    }

    static void dfs(Map<Integer, List<Integer>> graph, int start, Boolean[] visited) {
        if(!visited[start - 1]) {
            visited[start - 1] = true;

            if(graph.get(start) != null) {
                for(int j = 0; j < graph.get(start).size(); j++) {
                    if(!visited[graph.get(start).get(j) - 1]) {
                        dfs(graph, graph.get(start).get(j), visited);
                    }
                }
            }
            else {
                return;
            }
        }
    }
}
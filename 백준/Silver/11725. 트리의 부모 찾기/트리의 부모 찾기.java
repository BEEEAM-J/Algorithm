import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<List<Integer>> graph = new ArrayList<>();
    static int[] parentNodes;
    static boolean[] visited;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int i;
        int N = Integer.parseInt(br.readLine());
        parentNodes = new int[N];
        visited = new boolean[N + 1];

        for(i = 0; i < N; i++) {
            graph.add(new ArrayList<>());
        }

        for (i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int first = Integer.parseInt(st.nextToken());
            int second = Integer.parseInt(st.nextToken());

            graph.get(first - 1).add(second);
            graph.get(second - 1).add(first);
        }

        dfs(1);

        for(int k = 1; k < parentNodes.length; k++) {
            System.out.println(parentNodes[k]);
        }
    }

    public static void dfs(int node) {
        visited[node] = true;

        for(int n: graph.get(node - 1)) {
            if(!visited[n]) {
                parentNodes[n - 1] = node;
                dfs(n);
            }
        }
    }
}

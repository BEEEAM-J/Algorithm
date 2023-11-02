import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Map<Integer, Integer> people = new HashMap<>();

        int T = Integer.parseInt(br.readLine());
        int i, j, N, maxInterviewGrade;
        int res = 0;

        for (i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            for (j = 0; j < N; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                people.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            List<Integer> keyList = new ArrayList<>(people.keySet());
            Collections.sort(keyList);
            maxInterviewGrade = people.get(keyList.get(0));

            for (int key : keyList) {
                if (maxInterviewGrade >= people.get(key)) {
                    res += 1;
                    maxInterviewGrade = people.get(key);
                }
            }
            System.out.println(res);
            res = 0;
            people.clear();
        }
    }
}
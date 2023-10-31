import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<String> noHeard = new ArrayList<>();
        List<String> noHeardNoSee = new ArrayList<>();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int i;

        for (i = 0; i < N; i++) {
            noHeard.add(br.readLine());
        }

        Collections.sort(noHeard);

        for (i = 0; i < M; i++) {
            String inputPerson = br.readLine();

            if (Collections.binarySearch(noHeard, inputPerson) >= 0) {
                noHeardNoSee.add(inputPerson);
            }
        }
        Collections.sort(noHeardNoSee);

        System.out.println(noHeardNoSee.size());
//        bw.write("noHeardNoSee.size()");
//        bw.write("\n");
        for (String person: noHeardNoSee) {
//            System.out.println(person);
            bw.write(person);
            bw.write("\n");
        }
        bw.close();
    }
}
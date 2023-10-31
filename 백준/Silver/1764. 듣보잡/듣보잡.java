import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<String> noHeard = new ArrayList<>();
        List<String> noHeardNoSee = new ArrayList<>();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int i = 0;

        for (i = 0; i < N; i++) {
            noHeard.add(br.readLine());
        }

        Collections.sort(noHeard);

        for (i = 0; i < M; i++) {
            String inPerson = br.readLine();

            if (Collections.binarySearch(noHeard, inPerson) >= 0) {
                noHeardNoSee.add(inPerson);
            }
        }
        Collections.sort(noHeardNoSee);


        System.out.println(noHeardNoSee.size());
        for (String per: noHeardNoSee) {
            System.out.println(per);
        }
    }
}
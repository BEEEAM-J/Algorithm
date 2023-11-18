import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        long res = fibo(n);

        System.out.println(res);
    }

    private static long fibo(int n) {
        if (n <= 1) {
            return n;
        }

        long[] memo = new long[n + 1];
        memo[0] = 0;
        memo[1] = 1;

        for(int i = 2; i <= n; i++) {
            memo[i] = memo[i - 2] + memo[i - 1];
        }
        return memo[n];
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import static java.lang.Math.min;

public class Main {
    public static void main(String args[]) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1];

        dp[0] = 0;

        for(int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;

            for (int j = 1; j * j <= i; j++) {
                dp[i] = min(dp[i], dp[i - j * j] + 1);
            }
        }

        System.out.println(dp[n]);
    }
}
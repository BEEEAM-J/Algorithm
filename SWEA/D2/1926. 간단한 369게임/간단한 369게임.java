import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int num = 1; num <= N; num++)
        {
            String[] snList = String.valueOf(num).split("");
            int threeCnt = 0;
            int intNum = 0;

            for(int i = 0; i < snList.length; i++) {
                intNum = Integer.parseInt(snList[i]);

                if(intNum == 3 || intNum == 6 || intNum == 9) {
                    threeCnt += 1;
                }
            }
            switch (threeCnt) {
                case 0: {
                    System.out.print(num + " ");
                    break;
                }
                case 1: {
                    System.out.print("- ");
                    break;
                }
                case 2: {
                    System.out.print("-- ");
                    break;
                }
                case 3: {
                    System.out.print("--- ");
                    break;
                }
                default: {

                }
            }

        }
    }
}
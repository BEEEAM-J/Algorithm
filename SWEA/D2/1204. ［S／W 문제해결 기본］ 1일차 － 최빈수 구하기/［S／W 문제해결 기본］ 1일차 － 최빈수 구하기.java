/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        Map<String, Integer> numMap = new HashMap<String, Integer>();       // {key: 숫자, value: 빈도}

        for(int test_case = 1; test_case <= T; test_case++)
        {
            int tN = Integer.parseInt(br.readLine());
            String nums = br.readLine();
            String frequencyValue = "";

            String[] numArray = nums.split(" ");

            for (int i = 0; i < 1000; i++) {
                if (numMap.containsKey(numArray[i])) {
                    numMap.put(numArray[i], numMap.get(numArray[i]) + 1);
                }
                else {
                    numMap.put(numArray[i], 1);
                }
            }

            for (String key: numMap.keySet()) {  // map의 key들로 반복
                if (numMap.get(key) == Collections.max(numMap.values())) {      // key로 가져온 map의 value(빈도)와 value(빈도)의 최대값 비교, 같으면 최빈값
                    frequencyValue = key;
                }
            }

            System.out.println("#" + tN + " " + frequencyValue);
            
            numMap.clear();
        }
	}
}
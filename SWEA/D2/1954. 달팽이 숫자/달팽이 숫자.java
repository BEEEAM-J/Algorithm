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

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0}; 
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int N = sc.nextInt();
            int x = 0;
            int y = 0;
            int direction = 0;
            int[][] snail = new int[N][N];
            boolean[][] visit = new boolean[N][N];
            
            for (int i = 0; i < N; i++) {
             	for (int j = 0; j < N; j++) {
                 	visit[i][j] = false;   
                }
            }
            
            for (int i = 1; i <= (N * N); i++) {
				snail[x][y] = i;             		   
                visit[x][y] = true;
                
                int nx = x + dx[direction];
                int ny = y + dy[direction];
                
                // 벽에 부딪히는 경우
                if(nx >= N || ny >= N || nx < 0 || ny < 0  || visit[nx][ny] == true) {
                 	direction += 1;
                    if(direction == 4) {
                     	direction = 0;	   
                    }
                }
                
                x += dx[direction];
                y += dy[direction];
            }
            
            // 출력
            System.out.println("#" + test_case);
            for(int i = 0; i < N; i++) {
             	for(int j = 0; j < N; j++) {
                    System.out.print(snail[i][j] + " ");
                }
                System.out.println();
            }
            
		}
	}
}
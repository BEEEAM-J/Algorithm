package week2;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class BOJ9012 {
    public static void main(String[] args) {
        List<Character> check = new ArrayList<>();
        int res = 0;

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < t; i++) {
            String inputData = sc.nextLine();
            for (int j = 0; j < inputData.length(); j++) {
                if(inputData.charAt(j) == '(') {
                    check.add('(');
                }
                else if (inputData.charAt(j) == ')') {
                    if(check.isEmpty()) {
                        res = 1;
                        break;
                    }
                    check.remove(check.size() - 1);
                }
            }
            if(res == 1) {
                System.out.println("NO");
            }
            else if(check.isEmpty()){
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
            res = 0;
            check.clear();
        }
    }
}

// 첫 줄에서 검사할 문자열의 개수인 정수 t를 입력 받는다.
// 괄호가 닫혀야 올바른 괄호 문자열이다.
// 임의의 리스트를 만들고 for문을 돌면서 '('가 있으면 만든 리스트에 추가하였다.
// 그리고 ')'가 나오면 만들었던 리스트에서 값을 제거하였다. 
// 만약 임의의 리스트에 값이 없는데 ')'가 나온 경우에는 무조건 틀린 괄호이기 때문에 틀린 괄호라는 것을 알려주는 변수에 값을 바꾼다.
// 모든 연산이 끝나면 틀린 괄호를 표시하는 변수가 1인 경우부터 검사하여 확인하는 리스트의 비어있는지 여부 등을 확인하여 값을 출력한다. 

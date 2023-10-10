package week2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ10773 {
    public static void main(String[] args) {
        int k;
        int sum = 0;
        List<Integer> nums = new ArrayList<Integer>();

        Scanner sc = new Scanner(System.in);

        k = sc.nextInt();

        for(int i = 0; i < k; i++) {
            int inputNum = sc.nextInt();
            if (inputNum == 0) {
                nums.remove(nums.size() - 1);
            }
            else {
                nums.add(inputNum);
            }
        }

        if(nums.isEmpty()) {
            System.out.println(0);
        }
        else {
            for(int i = 0; i < nums.size(); i++) {
                sum += nums.get(i);
            }
            System.out.println(sum);
        }
    }
}

// 첫 줄에서 정수의 개수 K를 받는다. 
// 그리고 키보드로부터 입력 받는 값을 리스트에 저장하는 동작을 반복한다.
// 이 과정을 진행하는 중 입력 받은 값이 0이면 숫자를 저장하는 리스트의 맨 뒤 값을 제거한다. 
// 입력을 다 받으면 리스트의 총합을 연산하여 출력한다.

package week2;

import java.util.*;

public class BOJ1158 {
    public static void main(String[] args) {
        Deque<Integer> josephus = new ArrayDeque<>();
        List<Integer> removedNum = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        int cnt = 1;
        int n = sc.nextInt();
        int k = sc.nextInt();

        for (int i = 1; i <= n; i++){
            josephus.add(i);
        }

        while (true) {
            if(josephus.size() > 1) {
                for (int i = 0; i < k - 1; i++) {
                    josephus.addLast(josephus.remove());
                }
                removedNum.add(josephus.element());
                josephus.remove(josephus.element());
            }
            else {
                removedNum.add(josephus.element());
                break;
            }
        }

        System.out.print("<");
        for (int num: removedNum) {
            System.out.print(num);
            if (cnt < n) {
                System.out.print(", ");
                cnt ++;
            }
        }
        System.out.print(">");
    }
}

// 1부터 n까지의 사람들이 원으로 앉아있고 돌면서 K번째 사람을 제거한다.
// k번째 사람 전까지는 맨 앞의 사람을 맨 뒤로 옮기고 K번째 사람은 제거하는 동작을 반복한다.

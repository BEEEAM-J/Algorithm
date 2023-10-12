package week2;

import java.util.*;

public class BOJ1021 {
    public static void main(String[] args) {
        List<Integer> popNumber = new ArrayList<>();
        Deque<Integer> numberQueue = new ArrayDeque<>();
        Deque<Integer> numberLeftQueue = new ArrayDeque<>();
        Deque<Integer> numberRightQueue = new ArrayDeque<>();
        int res = 0;

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            popNumber.add(sc.nextInt());
        }

        for (int i = 1; i <= n; i++) {
            numberQueue.add(i);
        }
        numberLeftQueue.addAll(numberQueue);
        numberRightQueue.addAll(numberQueue);

        for (int i = 0; i < m; i++) {
            int moveToLeft = 0;
            int moveToRight = 0;

            while (true) {
                // 왼쪽으로 이동
                if (numberLeftQueue.element() == popNumber.get(i)) {
                    numberLeftQueue.removeFirst();
                    break;
                }
                else {
                    int firstElement = numberLeftQueue.removeFirst();
                    numberLeftQueue.addLast(firstElement);
                    moveToLeft += 1;
                }
            }

            while (true) {
                // 오른쪽으로 이동
                if (numberRightQueue.element() == popNumber.get(i)) {
                    numberRightQueue.removeFirst();
                    break;
                }
                else {
                    int lastElement = numberRightQueue.removeLast();
                    numberRightQueue.addFirst(lastElement);
                    moveToRight += 1;
                }
            }

            if (moveToLeft >= moveToRight) {
                numberLeftQueue.clear();
                numberLeftQueue.addAll(numberRightQueue);
                res += moveToRight;
            }
            else {
                numberRightQueue.clear();
                numberRightQueue.addAll(numberLeftQueue);
                res += moveToLeft;
            }
        }
        System.out.println(res);
    }
}

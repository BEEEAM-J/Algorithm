import java.util.*;

public class Main {
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
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.Stack;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> stack = new Stack<>();
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++) {
            String str = br.readLine();

            String[] order = str.split(" ");

            if(Objects.equals(order[0], "push")) {
                stack.push(Integer.parseInt(order[1]));
            } else if (Objects.equals(order[0], "pop")) {
                if(stack.empty()) {
                    System.out.println("-1");
                } else {
                    System.out.println(stack.pop());
                }

            } else if (Objects.equals(order[0], "size")) {
                System.out.println(stack.size());
            } else if (Objects.equals(order[0], "empty")) {
                if(stack.empty()) {
                    System.out.println("1");
                } else {
                    System.out.println("0");
                }
            } else if (Objects.equals(order[0], "top")) {
                if(stack.empty()) {
                    System.out.println("-1");
                } else {
                    System.out.println(stack.peek());
                }
            }
        }
    }
}

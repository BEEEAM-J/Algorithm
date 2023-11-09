import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        
        String[] arr = new String[numbers.length];
        StringBuilder sb = new StringBuilder();
        String answer = "";
        
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = Integer.toString(numbers[i]);
        }
        
        Arrays.sort(arr, (n1, n2) -> (n2 + n1).compareTo(n1 + n2));
        
        for (String str: arr) {
            sb.append(str);
        }
        
        answer = sb.toString();
        
        if(answer.charAt(0) == '0') answer = "0";
        
        return answer;
    }
}
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> res = new ArrayList();
        int previous = -1;
        int cnt = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] != previous) {
                cnt ++;
                res.add(arr[i]);
            }
            previous = arr[i];
        }
        int[] answer = new int[cnt];
        
        for(int j = 0; j < cnt; j++) {
            answer[j] = res.get(j);
        }
        
        return answer;
    }
}
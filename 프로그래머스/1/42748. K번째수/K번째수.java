import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> numbers = new ArrayList<>();
        int len = commands.length;
        // List<Integer> answer = new ArrayList<>();
        int[] answer = new int[len];
        int i, j, k;
        int idx = 0;
        
        for(int[] nums: commands) {
            i = nums[0];
            j = nums[1];
            k = nums[2];
            
            for(int m = i - 1; m < j; m++) {
                numbers.add(array[m]);
            }
            Collections.sort(numbers);
            answer[idx] = numbers.get(k - 1);
            numbers.clear();
            
            idx++;
        }
        return answer;
    }
}
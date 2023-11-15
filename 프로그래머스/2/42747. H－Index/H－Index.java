import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int cnt = 0;
        
        List<Integer> cList = new ArrayList();
        
        for (int v: citations) {
            cList.add(v);   
        }
        
        Collections.sort(cList, Collections.reverseOrder()); 
        
        int h;
        
        for (h = cList.get(0); h > 0; h--) {
            for (int value: cList) {
                // System.out.println("h: " + h + " value: " + value);
                if(value >= h) {
                    cnt += 1;
                }
                else {
                    break;
                }
                // System.out.println("cnt: " + cnt);
            }
            if(cnt >= h) {
                System.out.println(h);
                answer = h;
                break;
            }
            cnt = 0;
        }
        return answer;
    }
}
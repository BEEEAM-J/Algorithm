import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();
        int N = Integer.parseInt(br.readLine());
        int i, inputNum;
        int avg, mid, range;

        List<Integer> numbers = new ArrayList<>();
        List<Integer> frequencyList = new ArrayList<>();

        for (i = 0; i < N; i ++) {
            inputNum = Integer.parseInt(br.readLine());
            numbers.add(inputNum);
            if (frequencyMap.containsKey(inputNum)) {
                frequencyMap.put(inputNum, frequencyMap.get(inputNum) + 1);
            }
            else {
                frequencyMap.put(inputNum, 1);
            }
        }

        Collections.sort(numbers);

        avg = (int) Math.round(((double) (numbers.stream().mapToInt(Integer::intValue).sum()) / N));
        mid = numbers.get(N / 2);
        range = Collections.max(numbers) - Collections.min(numbers);

        for (int key: frequencyMap.keySet()) {
            if (frequencyMap.get(key) == Collections.max(frequencyMap.values())) {      // key로 가져온 map의 value와 value의 최대값 비교, 같으면 최빈값
                frequencyList.add(key);
            }
        }
        Collections.sort(frequencyList);

        System.out.println(avg);
        System.out.println(mid);
        if (frequencyList.size() > 1) {
            System.out.println(frequencyList.get(1));
        }
        else {
            System.out.println(frequencyList.get(0));
        }
        System.out.println(range);
    }
}
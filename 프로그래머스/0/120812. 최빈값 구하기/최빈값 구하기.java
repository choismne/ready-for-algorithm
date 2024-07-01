import java.util.HashSet;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int[] array) {
        HashSet<Integer> tmp = new HashSet<>();
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int value : array){
            tmp.add(value);
        }
        ArrayList<Integer> set = new ArrayList<>(tmp);
        System.out.println("SET :" + set);
        
        for (int target : set){
            int count = 0;
            for(int value : array){
                if(target == value){
                    count += 1;
                }
            }
            list.add(count);
        }
        System.out.println("LIST :" + list);
        
        int max = Collections.max(list); // 개수를 센거의 맥스값 . 그러니까 여기까지는 최빈값을 구한게 아니라 최빈값의 횟수를 구했구나
        
        //최빈값이 하나가 맞는지 확인
        int count = 0;
        for (int value : list){
            if(value == max){
                count +=1;
            }
        }
        
        
        if(count==1){
            int idx = list.indexOf(max);
            return set.get(idx);
        }
        else{
            return -1;
        }

    }
}
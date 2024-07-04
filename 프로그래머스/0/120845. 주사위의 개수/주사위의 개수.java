class Solution {
    public int solution(int[] box, int n) {
        int[] arr = new int[3];
        int answer = 1;
        for(int i=0 ; i<3 ; i++){
            arr[i] = box[i]/n;
        }
        for(int value : arr){
            answer *= value;
        }
        return answer;
    }
}
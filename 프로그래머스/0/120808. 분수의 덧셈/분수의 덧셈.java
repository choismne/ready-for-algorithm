class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numerator = numer1*denom2 + numer2*denom1;
        int denominator = denom1 * denom2;
        int gcd = gcd(numerator, denominator);
        int[] answer = {numerator/gcd, denominator/gcd};
        return answer;
    }
    private int gcd(int a, int b){
        while (b!=0){
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }
}
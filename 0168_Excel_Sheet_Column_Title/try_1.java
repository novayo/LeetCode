class Solution {
    public String convertToTitle(int n) {
        StringBuilder ans = new StringBuilder();
        while (n > 0){
            ans.append((char)((n-1)%26+65));
            n = (n-1)/26;
        }
        return ans.reverse().toString();
    }
}            

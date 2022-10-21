class Solution {
private:
    int reveses(int x){
        int sum=0;
        while(x>0){
            sum=((sum*10)+x%10);
            x=x/10;
        }
        return sum;
    }
    
public:
    bool sumOfNumberAndReverse(int num) {
        if (num == 0) return true;
        
        int target = num;
        while (num--) {
            int r_num = reveses(num);
            
            if (num + r_num == target) {
                return true;
            }
        }
        
        return false;
    }
};

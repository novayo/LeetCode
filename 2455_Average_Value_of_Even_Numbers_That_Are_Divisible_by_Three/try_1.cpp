class Solution {
public:
    int averageValue(vector<int>& nums) {
        int sum{0}, number{0};
        
        for (int& num : nums) {
            if (num % 2 == 0 && num % 3 == 0) {
                sum += num;
                number++;
            }
        }
        
        return number == 0 ? 0 : sum / number;
    }
};

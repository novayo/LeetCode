

int reverse(int x){
    int i, isPos=1, count=0;
    long ans = 0;
    if (x == -2147483648) return 0;
    if (x < 0){
        x *= -1;
        isPos = 0;
    }
    for (i=0; i<10; i++){
        int tmp = x / (int)pow(10, i);
        if (tmp == 0) break;
        ans *= 10;
        ans += tmp%10;
        if (ans > 2147483647) return 0;
    }
    
    if (isPos == 0) ans *= -1;
    return ans;
}



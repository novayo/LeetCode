int myAtoi(char * str){
    int i, len=strlen(str), numlen=0, isPos = 1, isSigned = 0, ans=0;
    for (i=0; i<len; i++){
        int atoi = (int)str[i]-48;
        if (ans == 0 && isSigned == 0 && atoi == -3){
            isSigned = 1;
            isPos = 0;
            continue;
        } else if (ans == 0 && isSigned == 0 && (atoi == -16 || atoi == -5)){
            if (atoi == -5) isSigned = 1;
            continue;
        }else if (atoi < 0 || atoi > 9) {
            break;
        }
        isSigned = 1;
        if (ans != 0) numlen++;
        if (numlen >= 9) {
            if (numlen == 9 && ((ans >= 214748364 && atoi > 7) || ans >= 214748370)){
                return (isPos==1?2147483647:-2147483648);
            } else if ((ans >= 214748364 && atoi > 7) || ans >= 214748370){
                return (isPos==1?2147483647:-2147483648);
            }
        }
        ans *= 10;
        ans += atoi;
    }
    
    return (isPos==1?ans:-ans);
}





char * longestPalindrome(char * s){
    int i, j;
    int len = strlen(s);
    int longest=-1, startIndex=-1;
    
    for (i=0; i<len; i++){
        if (longest > len - i) break;
        char pivot = s[i];
        for (j = len-1; j>i; j--){
            char compare = s[j];
            if (compare != pivot){
                continue;
            } else {
                int tmp_i = i, tmp_j = j, tmp_long = j-i+1;
                for (; tmp_i < tmp_j ; tmp_i++, tmp_j--){
                    if (s[tmp_i] != s[tmp_j]){
                        break;
                    }
                }
                if (tmp_i - tmp_j == 1 || tmp_i == tmp_j){
                    if (tmp_long > longest){
                        longest = tmp_long;
                        startIndex = i;
                    }
                }
            }
        }
    }
    
    char* ans = (char*)malloc(1001 * sizeof(char));
    memset(ans, '\0', 1001);
    for (i=0; i<longest; i++){
        ans[i] = s[startIndex+i];
    }
    
    if (longest == -1) {
        ans[0] = s[0];
        return ans;
    } else {
        return ans;
    }
}




int lengthOfLongestSubstring(char * s){
    int i, j, k, pivot = 0, ans = 0, len = strlen(s);
    int* arr = calloc(len, sizeof(int));
    
    for (i=0; i<len-1; i++){
        arr[pivot++] = (int)s[i];
        for (k=i+1; k<len; k++){
            int ascii_s = (int)s[k];
            for (j=0; j<pivot; j++){
                if (ascii_s == arr[j]){
                    break;
                }
            }
            if (j == pivot){
                arr[pivot++] = ascii_s;
            } else {
                break;
            }
        }
        if (pivot > ans){
            ans = pivot;
        }
        pivot = 0;
        memset(arr, 0, len);
    }
    
    if (len == 1) return 1;
    else return ans;
}


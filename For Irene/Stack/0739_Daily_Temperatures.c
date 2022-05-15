

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* tem, int temperaturesSize, int* returnSize){
    int mark = -1;
    int arr_temp[temperaturesSize];
    int arr_day[temperaturesSize];
    int *result = calloc(temperaturesSize, sizeof(int));
    *returnSize = temperaturesSize;
        
    for(int i = 0; i < temperaturesSize ; i++){
        if(mark == -1 || arr_temp[mark] >= tem[i]){
            arr_temp[++mark] = tem[i];
            arr_day[mark] = i;   
        }else{
            while(mark >= 0 && arr_temp[mark] < tem[i]){
                result[arr_day[mark]] = i - arrday[mark];
                mark--;
            }
            i--;
        }
    }
    return result;
}


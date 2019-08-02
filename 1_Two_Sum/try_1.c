

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i, j, isTarget=0;
    int *result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    for (i=0; i<numsSize-1; i++){
        for (j=i+1; j<numsSize; j++){
            if (nums[i]+nums[j] == target){
                result[0] = i;
                result[1] = j;
                isTarget = 1;
                break;
            }
        }
        if (isTarget == 1){
            break;
        }
    }
    
    return result;
}





double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int median_index=-1, totalNums = nums1Size+nums2Size;
    if (totalNums % 2 == 0){
        median_index = totalNums / 2;
    } else {
        median_index = totalNums / 2 + 1;
    }
    
    int i=0, j=0, tmp_median = 0;
    while(i!=nums1Size || j!=nums2Size){
        if (j == nums2Size || (i != nums1Size && nums1[i] <= nums2[j])){
            i++;
            if (i+j == median_index){
                if (totalNums % 2 == 0){
                    tmp_median = nums1[i-1];
                } else {
                    return (double)nums1[i-1];
                }
            } else if (i+j == median_index+1){
                return (double)(tmp_median+nums1[i-1])/2.0;
            }
        } else if (i == nums1Size || (j != nums2Size && nums1[i] > nums2[j])){
            j++;
            if (i+j == median_index){
                if (totalNums % 2 == 0){
                    tmp_median = nums2[j-1];
                } else {
                    return (double)nums2[j-1];
                }
            } else if (i+j == median_index+1){
                return (double)(tmp_median+nums2[j-1])/2.0;
            }
        }   
    }
    return -1.0;
}

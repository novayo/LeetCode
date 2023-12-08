function containsDuplicate(nums: number[]): boolean {
    // O(n) / O(n) - where n is the length of input array
    const visited_set = new Set<number>();
    
    for (const num of nums) {
        if (visited_set.has(num)) {
            return true;
        }
        visited_set.add(num);
    }
    
    return false;
};

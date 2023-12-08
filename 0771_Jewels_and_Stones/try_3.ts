function numJewelsInStones(jewels: string, stones: string): number {
    // O(n) / O(1) - where n is the length of the stones
    const jewels_set = new Set<string>(jewels);
    
    let ans = 0;
    for (const _s of stones) {
        if (jewels_set.has(_s)) {
            ans++;
        }
    }
    
    return ans;
};

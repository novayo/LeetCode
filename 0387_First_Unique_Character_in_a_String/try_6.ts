function firstUniqChar(s: string): number {
    // O(n) / O(1) - where n is the length of the input string
    let counter = {};
    for (const _s of s) {
        counter[_s] = (counter[_s] | 0) + 1;
    }
    
    for (let i = 0; i < s.length; i++) {
        if (counter[s[i]] === 1) {
            return i;
        }
    }
    return -1;
};

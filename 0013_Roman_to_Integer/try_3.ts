function romanToInt(s: string): number {
    // O(n) / O(n) - where n is the length of the input string
    const roman_map = new Map<string, number>([
        ['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000],
    ]);
    
    let ans = roman_map.get(s[0]);
    for (let i=1; i<s.length; i++) {
        // 加入目前的位置
        ans += roman_map.get(s[i]);
        
        // 再去判斷前一格要不要減掉
        if (roman_map.get(s[i-1]) < roman_map.get(s[i])) {
            ans -= 2 * roman_map.get(s[i-1]);
        }
    }
    
    return ans;
};

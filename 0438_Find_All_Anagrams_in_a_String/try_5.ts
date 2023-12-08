function isSameMap(a_map, b_map): boolean {
    if (a_map.size !== b_map.size) {
        return false;
    }
    
    for (let key of a_map.keys()) {
        if (!b_map.has(key)) {
            return false;
        }
        
        if (a_map.get(key) !== b_map.get(key)) {
            return false;
        }
    }
    
    return true;
}

function findAnagrams(s: string, p: string): number[] {
    // O(m) / O(1)
    if (s.length < p.length) {
        return [];
    }
    
    // 取P的種類
    const p_map = new Map<string, number>();
    for (const _p of p) {
        if (!p_map.has(_p)) {
            p_map.set(_p, 0);
        }
        p_map.set(_p, p_map.get(_p) + 1);
    }
    
    // Sliding window s
    let ans_list = [];
    
    //   - 建立初始dict
    const loop_map = new Map<string, number>();
    for (let i=0; i < p.length; i++) {
        if (!loop_map.has(s[i])) {
            loop_map.set(s[i], 0);
        }
        loop_map.set(s[i], loop_map.get(s[i]) + 1);
    }
    if (isSameMap(loop_map, p_map)) {
        ans_list.push(0);
    }
    
    //   - 往右邊移
    for (let j = p.length; j < s.length; j++) {
        const i = j - p.length;
        
        // 加入s[j]
        if (!loop_map.has(s[j])) {
            loop_map.set(s[j], 0);
        }
        loop_map.set(s[j], loop_map.get(s[j]) + 1);
        
        // 刪除s[i]
        loop_map.set(s[i], loop_map.get(s[i]) - 1);
        if (loop_map.get(s[i]) === 0) {
            loop_map.delete(s[i]);
        }
        
        // Compare
        if (isSameMap(loop_map, p_map)) {
            ans_list.push(i+1);
        }
    }
    
    return ans_list;
};



function uniqueOccurrences(arr: number[]): boolean {
    // O(n) / O(1) - where n is the length of the input array
    const occurrence_map = new Map<number, number>();
    for (const val of arr) {
        if (!occurrence_map.has(val)) {
            occurrence_map.set(val, 0);
        }
        occurrence_map.set(val, occurrence_map.get(val) + 1);
    }
    return occurrence_map.size === (new Set<number>(Array.from(occurrence_map.values()))).size;
};

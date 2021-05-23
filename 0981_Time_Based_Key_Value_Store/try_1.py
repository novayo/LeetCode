class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        target_list = self.table[key]
        index = self.bisect_left('set', key, timestamp) # 取得最左邊的index

        # 如果沒有設定過，就插入
        if len(target_list) == 0 or index >= len(target_list) or target_list[index][0] != timestamp:
            target_list.insert(index, [timestamp, value])
        # 如果設定的時間已經被設定過了，就取代舊的
        else:
            target_list[index][1] = value

    def get(self, key: str, timestamp: int) -> str:
        target_list = self.table[key]
        index = self.bisect_left('get', key, timestamp)

        if index == -1:
            return ''
        else:
            return target_list[index][1]

    def bisect_left(self, mode, key, timestamp):
        target_list = self.table[key]

        def condition(mid):
            mid_timestamp = target_list[mid][0]
            if mid_timestamp >= timestamp:
                return True
            else:
                return False
        
        left, right = 0, len(target_list)
        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        if mode == 'get':
            # 如果算出來超過原本長度，取得後一個index ([10, 20] => 取30，則會取到index=2)
            if left >= len(target_list):
                return left - 1
            # 如果相等則維持 ([10, 20] => 取20，則會取到index=1)
            elif target_list[left][0] == timestamp:
                return left
            # 往內算一格，取左邊的值 ([10, 20] => 取15，則會取到index=1)
            else:
                return left - 1
        else:
            return left

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
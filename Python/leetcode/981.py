class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.map:
            return res
        vals = list(self.map[key])
        low = 0
        high = len(vals) - 1
        while low <= high:
            mid = (low + high) // 2
            if timestamp >= vals[mid][1]:
                res = vals[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return res

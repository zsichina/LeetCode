from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.dp = {}
        self.dp_val = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dp:
            self.dp[key] = [timestamp]
            self.dp_val[key] = [value]
        else:
            self.dp[key].append(timestamp)
            self.dp_val[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dp:
            return ""
        idx = bisect_right(self.dp[key], timestamp)
        if self.dp[key][idx - 1] == timestamp:
            return self.dp_val[key][idx - 1]
        if idx == 0:
            return ""
        return self.dp_val[key][idx - 1]

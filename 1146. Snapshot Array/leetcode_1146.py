from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.changes = {}
        self.snaps = defaultdict(dict)
        self.snaps_cnt = 0

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val

    def snap(self) -> int:
        for key, val in self.changes.items():
            self.snaps[key][self.snaps_cnt] = val
        self.snaps_cnt += 1
        return self.snaps_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps and snap_id in self.snaps[index]:
            return self.snaps[index][snap_id]
        return 0


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(list)
        self.snap_cnt = 0

    def set(self, index: int, val: int) -> None:
        if self.snaps[index] and self.snaps[index][-1][0] == self.snap_cnt:
            self.snaps[index][-1][1] = val
        else:
            self.snaps[index].append([self.snap_cnt, val])

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        start, end, last_snap_id = 0, len(self.snaps[index]) - 1, -1
        while start <= end:
            mid = (start + end)//2
            if self.snaps[index][mid][0] <= snap_id:
                start = mid + 1
                last_snap_id = mid
            else:
                end = mid -1
                    
        return 0 if last_snap_id == -1 else self.snaps[index][last_snap_id][1]

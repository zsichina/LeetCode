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


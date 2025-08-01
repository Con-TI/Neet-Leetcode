class TimeMap:
    def __init__(self):
        self.data = dict() # key:{timestamp:[value1,value2],...}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1)
        key_dict = self.data.get(key,defaultdict(list))
        key_dict[timestamp].append(value)
        self.data[key] = key_dict

    def get(self, key: str, timestamp: int) -> str:
        # O(log n), binary search on avail timestamp
        if self.data.get(key,None) is None:
            return ""
        else:
            key_dict = self.data[key]
            timestamps = list(key_dict.keys())
            if timestamps[0] > timestamp:
                return ""

            # Get the most recent timestamp
            l,r = 0, len(timestamps) - 1

            idx = l
            while l<=r:
                m = (l+r)//2
                if timestamps[m] < timestamp:
                    idx = m
                    l = m + 1
                elif timestamps[m] > timestamp:
                    r = m-1
                else:
                    idx = m
                    break
            
            recent = timestamps[idx]

            # Query the timestamp
            return key_dict[recent][-1]

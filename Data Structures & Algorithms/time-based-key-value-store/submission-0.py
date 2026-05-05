class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([timestamp, value])        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:

            return ""

        values = self.keyStore[key]

        left = 0

        right = len(values) - 1

        result = ""

        # Find latest timestamp <= requested timestamp

        while left <= right:

            mid = (left + right) // 2

            mid_timestamp, mid_value = values[mid]

            if mid_timestamp <= timestamp:

                # Valid answer, but try to find a later valid timestamp

                result = mid_value

                left = mid + 1

            else:

                # Too far in the future

                right = mid - 1
    
        return result

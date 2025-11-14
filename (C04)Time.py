class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        self._normalize()

    def _normalize(self):
        # Handle seconds overflow
        self._minute += self._second // 60
        self._second = self._second % 60
        # Handle minutes overflow
        self._hour += self._minute // 60
        self._minute = self._minute % 60
        # If you want hours to wrap around 24:
        self._hour = self._hour % 24

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time(self._hour + other._hour,
                    self._minute + other._minute,
                    self._second + other._second)

    def __str__(self):
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"

# Example usage
if __name__ == "__main__":
    t1 = Time(2, 45, 50)
    t2 = Time(3, 20, 30)
    sum_time = t1 + t2

    print("Time 1:", t1)
    print("Time 2:", t2)
    print("Sum:", sum_time)

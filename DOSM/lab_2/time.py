class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds
    def __str__(self):
        return f"{self._seconds}s"
    def __int__(self):
        return self._seconds

class Minutes:
    def __init__(self, minutes):
        self._minutes = minutes
    def __str__(self):
        return f"{self._minutes}m"
    def __int__(self):
        return self._minutes

class Hours:
    def __init__(self, hours):
        self._hours = hours
    def __str__(self):
        return f"{self._hours}h"

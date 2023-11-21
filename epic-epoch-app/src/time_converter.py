from datetime import datetime

class TimeConverter:
    def __init__(self, time):
        self.time = time
        self.now = datetime.now()

    def millis_to_datetime(self, millis):
        return datetime.fromtimestamp(millis / 1000.0)

    def seconds_to_datetime(self, seconds):
        return datetime.fromtimestamp(seconds)

    def datetime_to_millis(self, dt):
        return int(dt.timestamp() * 1000)

    def datetime_to_seconds(self, dt):
        return int(dt.timestamp())
    
    def __str__(self) -> str:
        return str(self.now)


# converter = TimeConverter(0)
# print(converter.millis_to_datetime(1700000000000))
# print(converter.seconds_to_datetime(1700000000))
# print(converter.datetime_to_millis(datetime.now()))
# print(converter.datetime_to_seconds(datetime.now()))
# print(converter)

# print(converter.datetime_to_millis(datetime(year=2023,month=11,day=21)))
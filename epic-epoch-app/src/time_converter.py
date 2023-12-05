from datetime import datetime


class TimeConverter:
    def __init__(self):
        #self.time = time
        self.now = datetime.now()

    def millis_to_datetime(self, millis):
        #print("millis_to_datetime on kutsuttu",millis,datetime.fromtimestamp(millis / 1000.0))
        return datetime.fromtimestamp(millis / 1000.0)

    def seconds_to_datetime(self, seconds):
        #print("seconds_to_datetime on kutsuttu",seconds,datetime.fromtimestamp(seconds))
        return datetime.fromtimestamp(seconds)

    def datetime_to_millis(self, dt):
        return int(dt.timestamp() * 1000)

    def datetime_to_seconds(self, dt):
        return int(dt.timestamp())
    
    def __str__(self) -> str:
        return str(self.now)


time_converter = TimeConverter()
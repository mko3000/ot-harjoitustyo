import unittest
from datetime import datetime
from time_converter import TimeConverter

class TestTimeConverter(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = TimeConverter()
    
    def test_millis_to_datetime_correctly(self):
        self.assertEqual(self.converter.millis_to_datetime(1700517600000), datetime(year=2023,month=11,day=21))

    def test_seconds_datetime_correctly(self):
        self.assertEqual(self.converter.seconds_to_datetime(1700517600), datetime(year=2023,month=11,day=21))

    def test_datetime_to_millis_correctly(self):
        dt = datetime(year=2023,month=11,day=21)
        self.assertEqual(self.converter.datetime_to_millis(dt), 1700517600000)

    def test_datetime_to_seconds_correctly(self):
        dt = datetime(year=2023,month=11,day=21)
        self.assertEqual(self.converter.datetime_to_seconds(dt), 1700517600)
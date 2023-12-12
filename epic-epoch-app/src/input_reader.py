from time_converter import TimeConverter
from datetime import datetime, date


class InputReader:
    def __init__(self, input):
        self.converter = TimeConverter()
        self.input = input
        self.result = "empty"
        self.format = None
        current_time = datetime.now()
        self.years = current_time.year
        self.month = current_time.month
        self.day = current_time.day
        self.hour = current_time.hour
        self.minute = current_time.minute
        self.second = current_time.second
        self.delimitters = [" ",".","-",":"]
        self.convert()

    def read(self,input):
        self.input = input 
        
    def convert(self):
        self.result = self._recognize_format()
        #return self.result

    def _recognize_format(self):
        if self._converts_to_number(self.input):
            self.input = float(self.input)
            if self.input == 0:
                self.format = "milliseconds"
                return self.converter.millis_to_datetime(self.input)
            elif self._is_yyyymmdd(self.input):
                self.format = "date"  
                self._parse_yyyymmdd()
            elif self.input < 10000000000:
                self.format = "seconds" 
                return self.converter.seconds_to_datetime(self.input)
            elif self.input < 10000000000000:
                self.format = "milliseconds"
                return self.converter.millis_to_datetime(self.input)
            else:
                self.format = "not supported"
        elif self._is_datetime(self.input):
            self.format = "datetime"
        else: 
            self.format = "other"
        # elif self._is_datetime(self.input) or self._is_date(self.input) or self._is_time(self.input):
        #     print(f'case other')
        #     self.format = "other"
        # else:
        #     print(f'not supported')
        #     self.format = "not supprted"
        return self.format
    
    def _is_yyyymmdd(self,candidate):
        if candidate < 100000000 and candidate >= 10000000:
            if candidate % 100 != 0 and candidate % 10000 > 100:
                return True
        return False
    
    def _is_datetime(self,candidate):
        if ("-" in candidate or "." in candidate) and ":" in candidate and self._all_numbers(candidate):
            return True
        return False

    def _is_date(self,candidate):
        if ":" not in candidate:
            if "-" in candidate:
                parts = candidate.split("-")
            if "." in candidate:
                parts = candidate.split(".")
            for part in parts:
                if not self._converts_to_number(part):
                    return False
            return True
        return False
    
    def _is_time(self,candidate):
        if ("-" not in candidate and "." not in candidate) and ":" in candidate:
            return True
        return False 
    
    def _all_numbers(self,candidate):
        parts=self._get_parts(candidate)
        for part in parts:
            if not self._converts_to_number(part):
                return False
        return True
        
    def _get_parts(self,string_to_divide):
        parts=[string_to_divide]
        delimitters = [" ",".","-",":"]
        for d in delimitters:
            new_parts = []
            for part in parts:
                new_parts.extend(part.split(d))
            parts = new_parts
        return parts


    def _parse_yyyymmdd(self):
        this_date = self.input
        d = int(20230101 % 100)
        m = int((this_date - d)/100%100)
        y = int((this_date - m - d)/10000)
        self.year = y
        self.month = m
        self.day = d

    def _parse_datetime(self):
        pass
    
    def _parse_date(self):
        pass

    def _parse_time(self):
        pass

    def _build_datetime(self):
        return(datetime(self.year,self.month,self.day,self.hour,self.minute,self.second))

    def _build_date(self):
        return(date(self.year,self.month,self.day))

    def _converts_to_number(self, input):
        try:
            float(input)
            return True
        except:
            return False


    def read_timestamp():
        pass

    def __str__(self):
        return f'result: {self.result}'

#input_reader = InputReader()
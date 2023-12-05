from datetime import datetime, date
def is_datetime(candidate):
    if ("-" in candidate or "." in candidate) and ":" in candidate:
        return True
    return False

def is_date(candidate):
    if ("-" in candidate or "." in candidate) and ":" not in candidate:
        return True
    return False

def is_time(candidate):
    if ("-" not in candidate and "." not in candidate) and ":" in candidate:
        return True
    return False

def all_numbers(candidate):
    parts=[candidate]
    delimitters = [" ",".","-",":"]
    for d in delimitters:
        new_parts = []
        for part in parts:
            new_parts.extend(part.split(d))
            # split_part = part.split(d)
            # for s in split_part:
            #     new_parts.append(s)
        parts = new_parts
    return parts

print(all_numbers("2023-12-04 23:17:28"))
print("moi")

# parts = ['2023-12-04 23:17:28']
# results = []
# delimitters = [" ",".","-",":"]
# for d in delimitters:
#     for part in parts:        
#         #print(part.split(d))
#         split_part = part.split(d)
#         for s in split_part:
#             parts.append(s)
#         #results.append(part.split(d))

# print(parts)

inputs = ["2023-12-04 23:17:28","2023-12-04","04.12.2023","4.12.2023","23:27 12.04.2023","23:27 12.4.","23:27"]

# for test_date in inputs:
#     print(f'{test_date} is_datetime: {is_datetime(test_date)}')
#     print(f'{test_date} is_date: {is_date(test_date)}')
#     print(f'{test_date} is_time: {is_time(test_date)}')


# print(20230101 % 1000)
# date_input = 20230101
# d = int(20230101 % 100)
# print(f'day: {d}')
# m = int((date_input - d)/100%100)
# print(f'month: {m}')
# y = int((date_input - m - d)/10000)
# print(f'year: {y}')

# print(f'{d}.{m}.{y}')

# print(date(y,m,d))

# print(type("2023-01-01"))
# some_input = "2023-01-01"
# print(some_input.count("-"))

# try:
#     print(float("23:27")) 
# except:
#     print("oli virhe")

# a = float("123")
# if (a%1 == 0):
#     a = int(a)
# print (isinstance(a,int))
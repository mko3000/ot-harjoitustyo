from input_reader import InputReader
from time_converter import TimeConverter

def main():
    
    # inputs = ["0","1701234567","1701234567890","20231204","2023-12-04 23:17:28","2023-12-04","04.12.2023","4.12.2023","23:27 12.04.2023","23:27 12.4.","23:27","tänään"]
    # print(len(inputs))
    # for test_input in inputs:
    #     print(InputReader(test_input))


    while True:
        date_input = str(input("Input date or timestamp, type 'exit' to quit\n"))
        if date_input == "exit":
            break
        ukilja = InputReader(date_input)
        print(lukija)
        #lukija.read(1701724648)

        


if __name__ == "__main__":
    main()


#1701724648

def main():
    while True:
        date_input = input("Input date or timestamp, type 'exit' to quit\n")
        if date_input == "exit":
            break
        print(type(date_input))


if __name__ == "__main__":
    main()
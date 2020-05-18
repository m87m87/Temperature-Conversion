def temperature_conversion():
    while True:
        try:
            f = int(input("Enter your F here: "))
            break
        except ValueError:
            print("only number here")

    f1 = f - 32
    f2 = 5/9
    result_c = round(f1*f2)

    if result_c > 21:
        print(round(result_c), "It's kind of hot.")

    elif 8 <= result_c <= 20:
        print(round(result_c), "It's kind of chill")

    else:
        return print(result_c, "It's cold.")


temperature_conversion()


def once_more():
    while True:
        another = input("Do you want to convert another temp, y/n? ")

        if another == 'y':
            temperature_conversion()

        elif another == 'n':
            break
        else:
            print("Enter y or n")


once_more()

print("Thanks for using my temperature conversion")

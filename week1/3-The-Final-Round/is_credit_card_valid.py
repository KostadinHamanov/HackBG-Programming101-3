def is_credit_card_valid(number):
    number = [int(x) for x in str(number)]

    index = 0

    if len(number) % 2 != 0:
        while index < len(number):
            if index % 2 != 0:
                number[index] = number[index] * 2
            index += 1

        str_number = ""
        for position in range(len(number)):
            str_number += str(number[position])

        number = [int(x) for x in str_number]

    return sum(number) % 10 == 0


def main():
    print (is_credit_card_valid(79927398713))
    print (is_credit_card_valid(79927398715))

if __name__ == "__main__":
    main()

def encode_password():
    password = input("Enter an 8-digit password: ")
    encoded_password = ""

    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    print("Your password has been encoded and stored!\n")
    return encoded_password


def decode_password(coded_password):
    decoded_password = ''
    for digit in coded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def main():

    option = int(input("'Please enter an option: "))
    coded_password = None

    while option != 3:
        if option == 1:
            coded_password = encode_password()
        elif option == 2:
            decoded_password = decode_password(coded_password)
            print(decoded_password)
        else:
            print("Invalid selection, try again.\n")
        option = int(input("Please enter an option: "))



main()

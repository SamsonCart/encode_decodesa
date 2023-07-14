# Samson's Decode Function, practice and build space

def decode_password(encoded_password):

    decoded_password = ""

    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit

    return decoded_password


def main():
    encoded_password = "67891234"
    decoded_password = decode_password(encoded_password)
    print("Decoded password:", decoded_password)

main()


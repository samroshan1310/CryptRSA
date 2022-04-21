# Decryption of cipher text plain text using RSA algorithm with square and multiply method

print("Enter your Public Key N:")
public_key_n = int(input())
print("Enter your Private Key d:")
private_key_d = int(input())
print("Please enter the message you want to decrypt : ")
message = str(input())
message = message.replace('[', '')
message = message.replace(']', '')
values = message.split(",")


def square_and_multiply(string, d, N):
    flag = 1
    while d > 0:
        if d % 2 != 0:
            flag = (flag * string) % N
        string = (string * string) % N
        d = int(d / 2)

    return flag % N


cipher_to_int = []
int_to_hex = []
hex_to_ascii = []
decrypted_message = []

for i in values:
    sb = ''
    chunk = int(i)
    messageChunk = square_and_multiply(chunk, private_key_d, public_key_n)
    cipher_to_int.append(messageChunk)

    ciph_hex = hex(messageChunk)
    int_to_hex.append(ciph_hex)

    sb += ciph_hex.replace('0x', '')
    hex_ascii = bytes.fromhex(sb)
    temp = hex_ascii.decode("ASCII")
    hex_to_ascii.append(temp)
    decrypted_message = ""
    decrypted_message = decrypted_message.join(hex_to_ascii)

print('Decrypted message integer values are : ', cipher_to_int)
print('Corresponding hexadecimal values of decrypted integers : ', int_to_hex)
print('Decrypted message in 3-byte chunks : ', hex_to_ascii)
print('\n Decrypted message received from partner is :', decrypted_message)


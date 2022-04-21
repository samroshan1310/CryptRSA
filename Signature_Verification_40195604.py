# Verification of Partner's Signature and encrypted Signature Text
print("Enter your Partner's Public Key N:")
public_key_n = int(input())
print("Enter your Partner's Public Key e:")
public_key_e = int(input())
print("Enter your Partner's Signature")
signature = input()
print("Please enter your Partner's encrypted Signature for Verification : ")
message = str(input())
message = message.replace('[', '')
message = message.replace(']', '')
values = message.split(",")


def square_and_multiply(string, e, N):
    flag = 1
    while e > 0:
        if e % 2 != 0:
            flag = (flag * string) % N
        string = (string * string) % N
        e = int(e / 2)

    return flag % N


cipher_to_int = []
int_to_hex = []
hex_to_ascii = []
decrypted_message = []

for i in values:
    sb = ''
    chunk = int(i)
    messageChunk = square_and_multiply(chunk, public_key_e, public_key_n)
    cipher_to_int.append(messageChunk)

    ciph_hex = hex(messageChunk)
    int_to_hex.append(ciph_hex)

    sb += ciph_hex.replace('0x', '')
    hex_ascii = bytes.fromhex(sb)
    temp = hex_ascii.decode("ASCII")
    hex_to_ascii.append(temp)
    decrypted_message = ""
    decrypted_message = decrypted_message.join(hex_to_ascii)

if signature == decrypted_message:
    print(decrypted_message, "'s Signature is Verified and True")
else:
    print('Signature is not Verified and False')

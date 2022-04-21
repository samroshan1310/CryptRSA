# Encryption of plain text to cipher text using RSA algorithm with square and multiply method

print("Enter your Partner's Public Key N:")
public_key_n = int(input())
print("Enter your Partner's Public Key e:")
public_key_e = int(input())
print("Please enter the message you want to encrypt : ")
message = str(input())

# Dividing the message string into 3-Byte Chunks
list_1 = []
for i in range(0, len(message), 3):
    if len(message) - i > 3:
        substring = message[i:i + 3]
        list_1.append(substring)
    else:
        substring = message[i:]
        list_1.append(substring)
print('Original message divided into 3-byte chunks : ', list_1)

# Converting the chunks to Hex and integer values
hex_list = []
hex_to_int = []
for i in list_1:
    hex_value = i.encode("utf-8").hex()
    hex_list.append('0x' + hex_value)
    int_value = (int(hex_value, 16))
    hex_to_int.append(int_value)
print('Chunks in Hexadecimal string : ', hex_list)
print('After converting chunks to integers : ', hex_to_int)


# Using Square and Multiply method to encrypt data
def square_and_multiply(string, e, N):
    flag = 1
    while e > 0:
        if e % 2 != 0:
            flag = (flag * string) % N
        string = (string * string) % N
        e = int(e / 2)

    return flag % N


cipher_text = [square_and_multiply(i, public_key_e, public_key_n) for i in hex_to_int]
print('\n Cipher Text after encryption : ', cipher_text)

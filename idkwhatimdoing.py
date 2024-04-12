def encode(uinput):
    encode = []
    for i in range(len(uinput)):
        ndigit = int(uinput[i]) + 3
        encode.append(str(ndigit))

        final_encode = ''.join(encode)
    return final_encode

def decode(final_encode):
    decoded = ""
    for i in final_encode:
        i = int(i)
        i -= 3
        i = str(i)
        decoded += i
    return decoded

def main():
    while True:
            print('Menu')
            print('-------------')
            print('1. Encode')
            print('2. Decode')
            print('3. Quit')
            print('')
            a = input('Please enter an option: ')
            if a.isdigit():
                a = int(a)

            if a == 1:
                uinput = input('Please enter your password to encode: ')
                encoded = encode(uinput)
                print('Your password has been encoded and stored!')

            elif a == 2:
                decoded = decode(encoded)
                print(f'The encoded password is {encoded}, and the original password is {decoded}.')

            else:
                break

if __name__ == "__main__":
    main()

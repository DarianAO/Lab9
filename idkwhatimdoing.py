def menu():
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
            encode = []
            for i in range(len(uinput)):
                ndigit = int(uinput[i]) + 3
                encode.append(str(ndigit))

            final_encode = ''.join(encode)
            print('Your password has been encoded and stored!')

        elif a == 2:
            print(f'The encoded password is {final_encode}, and the original password is {uinput}.')

        else:
            break

if __init__ == "__main__":
    menu()
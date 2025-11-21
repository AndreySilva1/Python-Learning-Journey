# Calculation of the first digit of a CPF
# CPF: 746.824.890-70
# Collect the sum of the first 9 digits of the CPF
# multiplying each one by a decreasing counter starting at 10

# Example: 746.824.890-70 (746824890)
#     10  9  8  7  6  5  4  3  2
# *    7  4  6  8  2  4  8  9  0
#     70 36 48 56 12 20 32 27 0

# Add all results:
# 70+36+48+48+12+20+32+27+0 = 301
# Multiply the result by 10:
# 301 * 10 = 3010
# Get the remainder of the division by 11:
# 3010 % 11 = 7

# If the result is greater than 9:
#     the digit becomes 0
# Otherwise:
#     the digit is the result itself

# The first CPF digit is 7

# To validate, take the first nine digits, perform the calculation and compare with the full CPF
while True:

    cpf = input('Enter the nine, ten or eleven digits of your CPF: ').strip().replace('.', '').replace('-', '').replace(' ', '')

    # validate if it's numeric
    try:
        int(cpf)
    except:
        print('Enter numbers only!')
        continue

    # FIRST DIGIT (9 digits)
    if len(cpf) == 9:
        total = 0
        n = 10
        for i in range(9):
            total += int(cpf[i]) * n
            n -= 1

        total = (total * 10) % 11
        total = total if total <= 9 else 0

        print(f'The first CPF digit is: {total}')

    # SECOND DIGIT (10 digits)
    elif len(cpf) == 10:
        total = 0
        m = 11
        for i in range(10):
            total += int(cpf[i]) * m
            m -= 1

        total = (total * 10) % 11
        total = total if total <= 9 else 0

        print(f'The second CPF digit is: {total}')

    # FULL CPF (11 digits)
    elif len(cpf) == 11:

        # first digit
        total1 = 0
        n = 10
        for i in range(9):
            total1 += int(cpf[i]) * n
            n -= 1

        total1 = (total1 * 10) % 11
        total1 = total1 if total1 <= 9 else 0

        # second digit
        cpf_ten = f'{cpf[:9]}{total1}'
        total2 = 0
        m = 11
        for i in range(10):
            total2 += int(cpf_ten[i]) * m
            m -= 1

        total2 = (total2 * 10) % 11
        total2 = total2 if total2 <= 9 else 0

        cpf_check = f'{cpf[:9]}{total1}{total2}'

        if cpf_check == cpf:
            print('The CPF is valid!')
        else:
            print('The CPF is invalid!')

    else:
        print('Enter only 9, 10 or 11 digits!')


def function_A(a):
    tens = int(a / 10)
    ones = int(a % 10)
    ans_A = ""

    if tens != 0 and tens % 2 == 0:
        ans_A = ans_A + "Even" + str(tens)
    elif tens % 2 != 0:
        ans_A = ans_A + "Odd" + str(tens)

    if ones % 2 == 0:
        ans_A = ans_A + "Even" + str(ones)
    else:
        ans_A = ans_A + "Odd" + str(ones)

    print("Function A: "+ans_A)
    return ans_A


def function_B(ans_A):
    word = ""
    ans_B = ""

    for i in ans_A:
        if i.isnumeric():
            ans_B = ans_B + word[::-1].upper() + i
            word = ""
        else:
            word = word + i

    print("Function B: "+ans_B)
    return ans_B


def function_C(ans_B):
    ans_C = ""

    for i in ans_B:
        if i.isnumeric():
            ans_C = ans_C + i
        else:
            ans_C = ans_C + str(ord(i))

    print("Function C: "+ans_C)
    return ans_C


def function_D(ans_C):
    ascii = ""
    ans_D = ""
    i = 0

    while i < len(ans_C):
        ascii = ascii + str(ans_C[i])

        ascii_int = int(ascii)
        if len(ans_C)-1 == i:
            ans_D = ans_D + str((ans_C[i]))
        elif ascii_int >= 65 and ascii_int <= 90:
            ans_D = ans_D + chr(ascii_int)
            ascii = ""
        elif ascii_int > 90:
            ans_D = ans_D + ascii[0]
            ascii = ""
            i = i-2
        i += 1

    print("Function D: "+ans_D)
    return ans_D


def function_E(ans_D):
    word = ""
    ans_E = ""

    for i in ans_D:
        if i.isnumeric():
            word = word[::-1]
            word = word[0] + word[1:].lower() + i
            ans_E = ans_E + word
            word = ""
        else:
            word = word + i

    print("Function E: "+ans_E)
    return ans_E


def function_F(ans_E):
    ans_F = ''.join(filter(str.isdigit, ans_E))
    print("Function F: "+ans_F)
    return int(ans_F)

while True :
    number = input("Enter a number between 1 - 20: ")
    try:
        number_int = int(number)
    except:
        print("Numbers only")
        continue
    if number_int >= 1 and number_int <= 20:
        print("Number is: " + number)
        ans = function_A(int(number))
        ans = function_B(ans)
        ans = function_C(ans)
        ans = function_D(ans)
        ans = function_E(ans)
        number_int = function_F(ans)
        break
    else:
        print("The number must be between 1 - 20.")

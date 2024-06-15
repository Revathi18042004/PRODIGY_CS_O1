import string

alpha = string.ascii_lowercase + string.ascii_uppercase
sentence = list(input("Enter text:\n").lower())
a = input("Enter 'encrypt' to ENCRYPT, 'decrypt' to DECRYPT, 'exit' to EXIT the program \n").lower()
shift_no = int(input("Enter the shift number from 1 to 25: \n"))
end = False

while not end:

    if a == 'encrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new = (alpha.index(sentence[i]) + shift_no) % 26
                sentence[i] = alpha[new]
        print(''.join(map(str, sentence)))
        end = True

    elif a == 'decrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            else:
                new = (alpha.index(sentence[i]) - shift_no) % 26
                sentence[i] = alpha[new]
        print(''.join(map(str, sentence)))
        end = True
        
    else:
        dec = input("Invalid entry. Try again. Y for YES, N for NO: \n").lower()
        if dec == 'y':
            sentence = list(input("Enter text:\n").lower())
            a = input("Enter 'encrypt' to ENCRYPT, 'decrypt' to DECRYPT, 'exit' to EXIT the program \n").lower()
            shift_no = int(input("Enter the shift number from 1 to 25: \n"))
        else:
            end = True

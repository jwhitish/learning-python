#simple password strength checker

import re


userPW = str(input("Enter a password: "))


if len(userPW) < 8:
    print('Password is not long enough')
else:
    lowerTest = re.compile(r'[a-z]+')
    test1 = lowerTest.findall(userPW)
    if len(test1) > 0:
        print('has lower alpha')
        upperTest = re.compile(r'[A-Z]+')
        test2 = upperTest.findall(userPW)
        if len(test2) > 0:
            print('has upper alpha')
            numTest = re.compile(r'\d+')
            test3 = numTest.findall(userPW)
            if len(test3) > 0:
                print('has number')
                print('Password is secure.')
            else:
                print('Password does not contain a number')
        else:
            print('Password does not contain upper case letter')
    else:
        print('Password does not contain lower case letter')

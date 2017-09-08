#! /usr/bin/env python3

#a simple program that extracts phone numbers and email addresses from clipboard contents, prints the result, and copies extracted information to the clipboard

import re, pyperclip

#create regex to match ph
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

#create regex to match email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,4})                   # dot-something
    )''', re.VERBOSE)

#find all matches in both regexes
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#format the matched strings to paste if matches found
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

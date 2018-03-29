"""Write a function that takes a string and does the same
thing as the strip() string method. If no other arguments
are passed other than the string to strip, then whitespace
characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second
argument to the function will be removed from the string."""

#! /usr/bin/env python3

import re

string = input('Enter a string to strip: ')
char = input('Enter the characters to be stripped: ')


def regexStrip(string, char=None):
    if char is None:
        print('No value')                             
    else:
        print('char is ' + char)
        strip = re.compile(r'

regexStrip(string, char)

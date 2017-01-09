# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count <10:
        print "Number of donuts: %d" % count
    else:
        print "Number of donuts: many"

test = int(raw_input("Number of donuts: "))
donuts(test)


def both_ends(s):
def both_ends(s):
    if len(s) > 2:
        first = s[:2]
        last = s[-2:]
        print first + last
    else:
        print ""

string = raw_input("Type in a string: ")
both_ends(string)


def fix_start(s):
    first = s[:1]
    rest = s[1:]
    if first in s:
        print first + rest.replace(first,'*')

string = raw_input("Enter a string: ")
fix_start(string)


def mix_up(a, b):
    firsta = a[:2]
    firstb = b[:2]
    lasta = a[2:]
    lastb = b[2:]
    newa = firstb + lasta
    newb = firsta + lastb
    print newa, newb

first = raw_input("Enter a string with more than 2 characters: ")
second = raw_input("Enter a string with more than 2 characters: ")

mix_up(first,second)


def verbing(s):
    last = s[-3:]
    if len(s) > 2:
        if last == "ing":
            print s + "ly"
        else:
            print s + "ing"
    else:
        print s

string = raw_input("Enter a string: ")
verbing(string)


def not_bad(s):
  notindex = s.find('not')
  if notindex != -1:
    if s.find('bad') != -1:
      badindex = s.find('bad') + 3
      if notindex < badindex:
        removetext = s[notindex:badindex]
        print s.replace(removetext, 'good')
  else:
      print s

string = raw_input("Enter a phrase: ")
not_bad(string)


def front_back(a, b):
    bhalfa = -int(len(a)/2)
    fhalfa = len(a) + bhalfa
    fronta = a[:fhalfa]
    backa = a[bhalfa:]
    bhalfb = -int(len(b)/2)
    fhalfb = len(b) + bhalfb
    frontb = b[:fhalfb]
    backb = b[bhalfb:]
    print fronta + frontb + backa + backb
    

stringa = raw_input("Enter a string: ")
stringb = raw_input("Enter a string: ")
front_back(stringa,stringb)
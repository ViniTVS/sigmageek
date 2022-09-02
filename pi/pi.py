#!/usr/bin/python3
import math
import sys
import requests
import logging
import time

# check if number is prime (https://geekflare.com/prime-number-in-python/)
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

# check if array contains palindrome
def palindrome(array):
    a_len = len(array)
    for i in range(int(a_len/2) + 1):
        if array[i] != array[a_len - 1 - i]:
            return False
    return True


def getPiDigits(start, digits = 1000):
    url = "https://api.pi.delivery/v1/pi?start="+ str(start) + "&numberOfDigits=" + str(digits)
    response = requests.get(url, timeout=10)
    
    pi_string = ""
    try:
        response = requests.get(url)
        pi_string = response.json()['content']
    except:
        # maybe I'm making too many requests, they need a time
        time.sleep(5)
        return getPiDigits(start)

    return pi_string

# turn the array numbers into an actual number
def arrayToNum(array):
    string = ""
    # "build" a string with the digits on our array 
    for value in array:
        string = string + str(value)
    # and convert it to a number (it's not the best, but works)
    return int(string)

def main():
    # get pi digits using Google's pi API
    start_num = 0
    pi_string = getPiDigits(start_num)
    # array to help find palindromes
    array = []
    # just populate the array with the first 21 digits
    for i in range(21):
        array.append(pi_string[i])
    #check if the 1000 first digits are palindrome
    for i in range(21, len(pi_string)):
        if (palindrome(array)):
            if is_prime(arrayToNum(array)):
                print(val)
                return
        # if it's not what we want, remove the first value from the array and insert another
        array.pop(0)
        array.append(pi_string[i])

    # for every char in the pi_string
    while True:
        # get new digits
        start_num += 1000
        pi_string = getPiDigits(start_num)

        for i in range(len(pi_string)):
            if (palindrome(array)):
                val = arrayToNum(array)
                if is_prime(val):
                    logging.debug("Value: " + str(val))
                    print(val)
                    return
            # if it's not what we want, remove the first value from the array and insert another
            array.pop(0)
            array.append(pi_string[i])
        

        
if __name__ == "__main__": 
    main()

#!/usr/bin/python3
import math
import requests
import logging

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

# turn the array numbers into an actual number
def arrayToNum(array):
    string = ""
    # "build" a string with the digits on our array 
    for value in array:
        string = string + str(value)
    # and convert it to a number (it's not the best, but works)
    return int(string)

def main():
    # some logging fro debugg
    logging.basicConfig(filename='pi.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    # get pi digits using Google's pi API
    url = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000"
    response = requests.get(url)
    pi_string = response.json()['content']
    # array to help find palindromes
    array = []
    # just populate the array with the first 21 digits
    for i in range(21):
        array.append(pi_string[i])
    #check if the 1000 first digits are palindrome
    for i in range(21, len(pi_string)):
        if (palindrome(array)):
            val = arrayToNum(array)
            if is_prime(val):
                print(val)
                return
    logging.debug("Start_num: " + str(start_num))
    logging.debug("Digits: " + pi_string)

    # for every char in the pi_string
    start_num = 0
    while True:
        # get new digits
        start_num += 1000
        url = "https://api.pi.delivery/v1/pi?start="+ str(start_num) + "&numberOfDigits=1000"
        response = requests.get(url)
        pi_string = response.json()['content']

        logging.debug("Start_num: " + str(start_num))
        logging.debug("Digits: " + pi_string)

        for i in range(len(pi_string)):
            if (palindrome(array)):
                val = arrayToNum(array)
                if is_prime(val):
                    print(val)
                    return
            # if it's not what we want, remove the first value from the array and insert another
            array.pop(0)
            array.append(pi_string[i])
        

        
if __name__ == "__main__": 
    main()
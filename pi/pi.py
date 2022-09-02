#!/usr/bin/python3
import math
import sys
import requests

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
    # noone said to find pi, so I can just use what other people made :)
    # pi value with 1 million digits, from http://www.eveandersson.com/pi/digits/1000000
    
    url = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000"
    response = requests.get(url)
    pi_string = response.json()['content']
    # array to help find palindromes
    array = []
    # just populate the array with the first 9 digits
    for i in range(21):
        array.append(pi_string[i])
    # for every char in the pi_string
    start_num = 0
    count = 1
    while True:
        print(count)
        count += 1
        # url = 
        for i in range(len(pi_string)):
            if (palindrome(array)):
                val = arrayToNum(array)
                if is_prime(val):
                    print(val)
                    break
            # if it's not what we want, remove the first value from the array and insert another
            array.pop(0)
            array.append(pi_string[i])
        
        start_num += 1000
        url = "https://api.pi.delivery/v1/pi?start="+ str(start_num) + "&numberOfDigits=1000"
        response = requests.get(url)
        pi_string = response.json()['content']
        

        
if __name__ == "__main__": 
    main()
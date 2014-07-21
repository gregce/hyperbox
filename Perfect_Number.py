#!/usr/bin/python -t
# Perfect Numbers

__author__ = 'gregce@gmail.com (Greg Ceccarelli)'


def divisors(number):
    divisor_list = []
    for i in range(1,number):
        if number % i == 0:
            divisor_list.append(i)
    return divisor_list

def evaluate_perfect(number):
    summy = sum(divisors(number))
    if summy == number:
        print '%d is a Perfect Number because %d = %d' % (number, summy, number)
    #elif summy > number:
    #    print '%d is an Abundant Number because %d > %d' % (number, summy, number)
    #else:
    #      print '%d is a Deficient Number because %d < %d' % (number, summy, number)
    return

import time
start_time = time.time()

for i in range(10000):
    evaluate_perfect(i)
    

print '--- %d seconds ---' % (time.time() - start_time)
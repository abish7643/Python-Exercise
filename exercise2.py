# Find 3 largest 9 digit palindrome prime numbers

import time
start_time = time.time()

"""

smallest_number = 100000001
largest_number = 999999999
largest_palindrome_number = 999999999
palindrome_prime_array = []

for i in range(largest_number, smallest_number, -1):

    # Check Whether Palindrome
    number = i
    print(number)
    string = str(i)
    reversedString = string[::-1]
    if string == reversedString:
        for j in range(2, largest_number-1, 1):
            # print(j)
            # Checking for prime

            prime_number = True
            if (i % j == 0 or i % 10 == 2 or i % 10 == 4 or i % 10 == 6 or i % 10 == 8):
                prime_number = False
                break

        if prime_number == True:
            # append to list if palindrome
            palindrome_prime_array.append(number)
    
    if (len(palindrome_prime_array) >= 3):
        break

print(palindrome_prime_array)

"""

"""
smallest_number = 100000001
largest_number = 999999999
largest_palindrome_number = 999999999
palindrome_prime_array = []
singleDigitArray = []


for i in range(largest_number, smallest_number, -1):
    
    if (len(palindrome_prime_array) >= 3):
        break

    # Check Whether Palindrome
    number = i
    print(number)
    string = str(i)
    reversedString = string[::-1]

    if string == reversedString:
        singleDigitArray = [int(x) for x in reversedString] #String into List of Integer Digits
        for j in singleDigitArray[:2]:
            #Get Factors of Each Digits
            # print(j)
            for k in range(2, 9, 1):
                prime_number = True
                if j%k == 0:
                    prime_number = False
                    break

        if prime_number == True:
            palindrome_prime_array.append(number)
            print("-------------Palindrome Prime No: {}-----------".format(number))
            
print(palindrome_prime_array)


print("--- %s seconds ---" % (time.time() - start_time))


# 10 999989999, 999979999, 999959999]

"""

"""
smallest_number = 100030000
largest_number = 100111002
largest_palindrome_number = 999999999
palindrome_prime_array = []
singleDigitArray = []



for i in range(largest_number, smallest_number, -1):
    
    if (len(palindrome_prime_array) >= 6):
        break

    # Check Whether Palindrome
    number = i
    #print(number)
    string = str(i)
    reversedString = string[::-1]
    count = 0
    
    singleDigitArray = [int(x) for x in reversedString] #String into List of Integer Digits
    for j in singleDigitArray:

        #Get Factors of Each Digits
        # print(j)
        for k in range(2, 9, 1):
            for l in range(2, 9, 1):
                if (j == k*l):
                    #print(j)
                    #print(singleDigitArray)
                    prime_number = False
                    count += 1
                    #print("---{}*{}---".format(k, l))
                    #print(count)

    if count == 0 and (string == reversedString):
        palindrome_prime_array.append(number)
        print("-------------Palindrome Prime No: {}-----------".format(number))
        
print(palindrome_prime_array)
"""



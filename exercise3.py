# Write a function to find all the pairs in the array whose sums already exist in array.
#          [10, 4, 8, 13, 5,4]  -> expected output is [(4,4),(8,5)]

"""
Two Interation Variables To Remove From Array For Checking Sum with Left List Items.

If Sum = list item: then add value of iteration variables as tuple to a list

"""

import time
start_time = time.time()

list_to_check = [10, 4, 8, 13, 5,4]
array_tuples = []

for i in range(len(list_to_check)):

    #i is the index of list iterating through
    i_number = list_to_check[i] #First Number
    print("----i_num = {}-------".format(i_number))

    # Pop Removes From The Original List if Copy Method is not used
    i_rm_list = list_to_check.copy()
    i_rm_list.pop(i)

    for j in range(len(i_rm_list)):

        j_number = i_rm_list[j] #Second Number

        j_rm_list = i_rm_list.copy()
        j_rm_list.pop(j)

        #Adding First and Second Number
        sum_numbers = i_number + j_number
        for k in j_rm_list:

            #Checking For Sum in list without both number taken into consideration
            if (sum_numbers == k):
                i_j_tuple = (i_number, j_number)
                print("-------{}-------".format(i_j_tuple))
                i_j_tuple_reversed = (i_number, j_number)[::-1]
                if i_j_tuple_reversed not in array_tuples:
                    array_tuples.append(i_j_tuple)
                break
        

print(array_tuples)

print("--- %s seconds ---" % (time.time() - start_time))

        

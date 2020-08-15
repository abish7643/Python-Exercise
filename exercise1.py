import time
start_time1 = time.time()

# Find the third smallest number in an unsorted array without using sort function. 
# Expected solution is of O(n)

#Best Method ( Expected solution is of O(n) )
print("------------Best Method--------------")

def SmallestThreeNumbers(numberslist, lengthoflist):
    firstmin = secondmin = thirdmin = 10000

    for i in range(0, lengthoflist):
        print('----------{} Loop------------'.format(i+1))
        print('-----------n = {}------------'.format(numberslist[i]))
        print('------{}-----{}-----{}-------'.format(firstmin, secondmin, thirdmin))
  
        if numberslist[i] < firstmin:
            thirdmin = secondmin
            secondmin = firstmin
            firstmin = numberslist[i]
            print('------{}-----{}-----{}-------'.format(firstmin, secondmin, thirdmin))

        elif numberslist[i] < secondmin:
            thirdmin = secondmin
            secondmin = numberslist[i]
            print('------{}-----{}-----{}-------'.format(firstmin, secondmin, thirdmin))
            
        elif numberslist[i] < thirdmin:
            thirdmin = numberslist[i]
            print('------{}-----{}-----{}-------'.format(firstmin, secondmin, thirdmin))
        
        print('------------end--------------')
  
    print([firstmin, secondmin, thirdmin])

  
numberslist = [4, 8, 6, 12, 2]
lengthoflist = len(numberslist)
SmallestThreeNumbers(numberslist, lengthoflist)

print("--- %s seconds ---" % (time.time() - start_time1))


start_time2 = time.time()

#--------------Sort Method----------------
print("-----------Sort Method-----------")


numberslist = [4, 8, 6, 12, 2]
sortmethodlist = numberslist
sortmethodlist.sort()
# sortmethodlist.sort(reverse=True)
print(sortmethodlist[:3])


print("--- %s seconds ---" % (time.time() - start_time2))



start_time3 = time.time()

#---------------Usual Loop Method------------
print("-----------Another Method-----------")


looplist = []
numberslist = [4, 8, 6, 12, 2]

while numberslist and len(looplist) < 3:
    let_min_number = numberslist[0]
    for i in numberslist:
        if i < let_min_number:
            let_min_number = i
    looplist.append(let_min_number)
    numberslist.remove(let_min_number)

print(looplist)
print("--- %s seconds ---" % (time.time() - start_time3))


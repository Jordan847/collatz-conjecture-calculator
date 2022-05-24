import math
import time
i = 1
while True:
    if  i==1:
        i+=1
    else:
        print("\n")
    number = int(input("enter number: ")); 
    amountofnumbers = 0
    highestnumber = []
    while  number > 1:
        if (number % 2) == 0:
         number /= 2
        else:
            number *= 3
            number += 1
        number = math.trunc(number)
        print ('{:,}'.format(number))
        amountofnumbers += 1 
        highestnumber.append(number)
        time.sleep(0.2)
    if number == 1:
        print(f"\nit took {amountofnumbers} steps to reach 1")
        highestnumber = max(highestnumber)
        highestnumber = '{:,}'.format(highestnumber)
        print(f"{highestnumber} was the highest number")
        
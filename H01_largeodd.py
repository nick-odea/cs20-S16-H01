# H01_largeodd.py    SOLO, Nick O'Dea, nicholas_odea@umail.ucsb.edu
# Homework 1, problem 5, CS20, Spring 2016


def largeodds():
    i = 1
    numb_largest = "There wasn't a largest odd number, as there weren't any odd numbers."
    while i<11:
        numb_new = raw_input("Please put in integer number" + str(i) + ": ")

        #I had strange results if the odd numbers were large,
        #such that a large odd modulo 2 is not 1 but 1L. Thus I have two cases
        #for checking if a number is odd.
        
        #The first odd number is the new largest odd number
        if type(numb_largest) == str:
            if int(numb_new) % 2 == 1 or int(numb_new) % 2 == 1L:
                numb_largest = numb_new
                
        #Subsequent odd numbers are the largest odd number only after checking that they are indeed the largest.
        else:
            if (int(numb_new) % 2 == 1 or int(numb_new) % 2 == 1L) and numb_new > numb_largest:
                numb_largest = numb_new
        i = i + 1
    print "Largest odd number: " +  numb_largest
    return
    



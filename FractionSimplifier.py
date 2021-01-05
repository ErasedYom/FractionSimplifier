# Python chode starts with a while loop for user input data, to also check if the user enters the correct values.
while True:
    n=input('Enter a numerator: ')
    d=input('Enter a denominator: ')
    # Asks user input to set the values for the numerator, and denominator.
    
    num = float(n)
    den = float(d)
    # set numerator, and denominator is to float since we want to accept .0 .
    
    if not (num).is_integer():  
        print('Invalid, please enter an integer')
    elif not (den).is_integer():   
        print('Invalid, Please enter an integer')
    # The two if loop is used to checks whether the float is int equivalent.
    # since 1.0 is the same as 1.
    # If the float num or den, has a greater decimal value than .0 e.g. 1.7, the user is required to set a new value int equivalent.
    
    else:
        if num == 0:
            print('The result is zero')
            break
        elif den == 0:
            print('The result is undetermined')
            break
    # This else if block of code is used to check wether there is a zero on either the numerator, or denominator.
    # If the num is zero the result would be zero, if the denominator is zero, the result is undetermined.
    # This is done because this would the result if a numerator/denominator is zero.
    
        else:
            break
    # else break is used to stop the while loop
    # If none of the previous if else condition was met, it means the user entered the correct values so we break out of the loop.



i = 2
# I = 2 is used as a starting value to divide

while True :
    if num == 0:
        break
    if den == 0:
        break
    # These 2 if statements is used so that this while loop doesn't continue,
    # if the values for either numerator or denominator is 0

    # while loop is used to go through the numbers that is divisable by numerator and denominator.
    a = num / i
    b = den / i
    if num > den and i > num :
        if num < 0 and den < 0:
            aa = abs(num)
            bb = abs(den)
            print( 'The result is: ', aa, '/', bb)
            break
        # if statement used to print -x/-x to x/x 
        else:
            print('The result is: ', num, '/', den)
            break
        
    if den > num and i > den:
        if num < 0 and den < 0:
            aa = abs(num)
            bb = abs(den)
            print( 'The result is: ', aa, '/', bb)
            break
        # if statement used to print -x/-x to x/x 
        else:
            print ('The result is: ', num, '/', den)
            break
    #This if, elif statement is used to check if I is greater than numerator, or denominator.
    #If I is greater than the simplification process will be stopped,
    #and print the simplest value of numerator and denominator.

    # While loop starts off by dividing num, and denominator by i(which would be 2 in its first iteration). 
    if a.is_integer() and b.is_integer():
    # This if loop is checked wether the i(2 in its first iteration) divided into the numerator and denominator returns an int.
    # If both numerator, and denominator returns an int or int equivalent (.0) it means its divisable by both.
    # So then this if statement block of code is executed if both numerator, denominator returns an int. 
        num = a
        den = b
        # Numerator is set to a(which is varible), since (a) was used to divide numerator by (I),
        # The simplified numerator is then used as a new value for the numerator.
        # This is done so that the new simplified value could be simplified again.
        # The same process is done with the denominator by with the variable (b).
    elif i != 2 : 
        i = i + 2  
    elif i == 2 :  
        i = i + 1
    # This elif block of code is used to increment I (which is 2), once on value is used to simplify e.g. 2,
    # its then increased i to check if the values could be simplified again with the new values to a point
    # where it no longer can be simplified.
    # code initially created to go through 2,3,5,7 dividing the numerator, and denominator until none of the
    # four fundementals could be divided by numerator and denominator.


    














    

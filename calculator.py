import array
keep_going = 'yes'
operation = 'z'
while keep_going == 'yes' or keep_going == 'y' or keep_going == 'Y' or keep_going == 'Yes':
    while operation == 'z':
        print ('What operation would you like to do?')
        print ('Press a to add.')
        print ('Press s to subtract.')
        print ('Press m to multiply.')
        print ('Press d to divide.')
        print ('Press p to percent (type in the numerator first).')
        choice = str(raw_input(':'))
        if choice == 'a':
            operation = 'add'
        elif choice == 's':
            operation = 'subtract'
        elif choice == 'm':
            operation = 'multiply'
        elif choice == 'd':
            operation = 'divide'
        elif choice == 'p':
            operation = 'p'
        else:
            print ('Thats not one of the choices.')
            operation = 'z'
    numbera = float(raw_input('Enter your first number:'))
    numberb = float(raw_input('Enter your second number:'))
    if choice == 'a':
        answer = numbera + numberb
    if choice == 's':
        answer = numbera - numberb
    if choice == 'm':
        answer = numbera * numberb
    if choice == 'd':
        answer = numbera / numberb
    if choice == 'p':
        answer = (numbera / numberb) * 100
    print ('Thats not one of the choices.')
    print ('\nYour answer is: %f' % (answer))
    operation = 'z'
    print ('\nWould you like to do more calculations? Type in yes or no.')
    keep_going = str(raw_input(':'))
print ('Okay. I hope I have been a helpful calculator.')
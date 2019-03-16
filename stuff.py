print('What is your name?')
name = str(raw_input(':'))
print('\nHello %s' %name)
print('How old are you?')
age = int(raw_input(':'))
print('What is a different persons name?')
name2 = str(raw_input(':'))
print('How old is %s?' %name2)
age2 = int(raw_input(':'))
if age > age2:
    difference = age-age2
    if difference == 1:
        print('\nYou are %d year older than %s.' % (difference, name2))
    if difference < 1:
            print('\nYou are %d years older than %s.' % (difference, name2))
if age2 > age:
    difference = age2-age
    if difference == 1:
        print('\n%s is %d year older than you.' % (name2, difference))
    if difference < 1:
        print('\n%s is %d years older than you.' % (name2, difference))
if age == age2:
    print('\nYou and %s are the same age.' % (name2))
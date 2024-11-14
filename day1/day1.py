import sys
first_input = input('hello ! Welcome to Band name generator (press any key to continue, or q to quit)')
if first_input == 'q':
    sys.exit()

first_name = input("hello, what's your place of birth : ")
last_name = input("oh that's great now, what's your pet name : ")

print('the band name suggestion for you is : '+first_name + ' '+ last_name)
# sum = 0
# for number in range(1,101):
#     sum+=number
# print(sum)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('welcome to PyPassword !')
number_of_letters = int(input('plz input number of letters you would like to have : '))
number_of_symbols = int(input(f'how many symbolls in this password ? '))
number_of_numbers = int(input(f'how many numbers in this length password ? '))

password = ''

for x in range(number_of_letters):
    password+=(letters[random.randint(0,len(letters)-1)])
for x in range(number_of_symbols):
    password+=(symbols[random.randint(0,len(symbols)-1)])
for x in range(number_of_numbers):
    password+=(numbers[random.randint(0,len(numbers)-1)])

random_password = []

while len(password):
    i = random.randint(0,len(password)-1)
    k = password[i]
    password = password[:i]+password[i+1:]


    random_password.append(k)


print('your password is: ')
print(''.join(random_password))
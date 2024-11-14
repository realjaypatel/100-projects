print("welcome to jay's pizza")
size = input("hello, what size of pizza would you like to order S, M, L : ")
peperoni = input("great, what about peperoni on your Pizza? Y or N : ")
extra_chese = input("okay, what extra chese? Y or N : ")

total = 0
# if size == 'S':
#     total +=15
#     if peperoni == 'Y':
#         total+=2
#     if extra_chese =='Y':
#         total+=1

# elif size == 'M':
#     total +=20
#     if peperoni == 'Y':
#         total+=3
#     if extra_chese =='Y':
#         total+=1
# elif size == 'L':
#     total +=25
#     if peperoni == 'Y':
#         total+=3
#     if extra_chese =='Y':
#         total+=1
# else:
#     print('you type wrong input')


    
if size == 'S':
    total+=15
elif size == 'M':
    total+=20
elif size == 'L':
    total+=25
else:
    print('type correct input')


if peperoni == 'Y':
    if size =='S':
        total+=2
    else:
        total+=3
if extra_chese == 'Y':
    total+=1



print(f"Your final bill is ${total}")
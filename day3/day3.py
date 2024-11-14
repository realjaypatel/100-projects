print('welcome to roller coster!')

customer_height = int(input("hii, plz input your height : "))
bill = 0

if customer_height > 180:
    print('oh great')
    customer_age = int(input('now plz enter your age for tickit'))
    if customer_age <8:
        bill+=6
        print('tickit price is 6$')
    elif customer_age <12:
        print('tickit price is 8$')
        bill+=8
    elif 45< customer_age<=55:
        print('have a ride on us')
    else:
        print('tickit price is 10$')
        bill+=10
    

    photo_required = input('want your photo in the roller coster ride (press y for Yes, and n for No)')
    if photo_required =='y':
        bill+=3
        print('great, you have to pay 3$ extra')
    print('thankyou, your total bill is : ', bill)

else:
    print("oh sorry, your height dosn't match our guidelint, try again next year")
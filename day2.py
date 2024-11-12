print('wellcome to tip calculator !')

total_bill = int(input("hey!, what's the total bill : "))
tip_amount = int(input('so, what percent of  tip you want to give (chose like 10 for 10%) : '))
number_of_people = int(input("okay, now how many people to split the bill : "))


print('so, yeah, each person should give' , (total_bill+((total_bill*tip_amount)/100))/number_of_people ,'$')
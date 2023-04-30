#  make a variable and assign a value 
# if user guess this number correctly then user win 
# if user guess the numbers is less than winnig_number print too low
# if user guess the number is greter than winning_number print too high 

winning_number=20
num=int(input("enter the number between 1 to 100 : "))
if winning_number==num:
    print("you win :")

elif winning_number<num:
    print("too high")

else:
    print("too low")
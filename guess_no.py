# actual_no=88
# attempts=0
# while True:
#     attempts+=1
#     guess_no=int(input("Enter your number"))
#     if(guess_no<actual_no):
#         print("Your guess was bit low")
#     elif(guess_no>actual_no):
#         print("Your guess was bit high")
#     elif (guess_no==actual_no):
#         print(f"Your guess was absolutely right in an attempt no.{attempts}")
#         break    
# print("Thank you")



import random
def guess(x):
    random_number = random.randint(1, x)
    # guess = 0
    # guess = int(input(f'Guess a number between 1 and {x}: '))
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
# a=guess(4)
# print(a)
print("WElcome")
guess(4)

# import random
# user=input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
# comp=random.choice(['r','p','s'])
# print(f"computer select {comp}")
# you_won,comp_won=0,0
# i=0
# print(f"round",i,"started")
# if(user==comp):
#     print("Its a tie")
#     you_won+=0
#     comp_won+=0
# elif(user=='r' and comp=='s') or (user=='p' and comp=='r') or (user=='s' and comp=='p'):
#         print("User won")
#         you_won+=1
# else:
#         print("Computerwon")
#         comp_won+=0          

# if(you_won>comp_won):
#     print("Congratulation!!!!!")
# else:
#     print("Sorry, better luck next time")
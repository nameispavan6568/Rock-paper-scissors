rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# rock = 0
# paper = 1
# scissors = 2
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
#Write your code below this line 👇
game_images = [rock,paper,scissors]
import random
user_input = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
print("Your Choice")
print(game_images[user_input])

computer_choice = random.randint(0,2)
print("computer_choice")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0: 
  print("You typed an invalid number, you lose!") 
elif user_input==0 and computer_choice==2:
  print("You win!")
elif user_input==2 and computer_choice==0:
  print("You lost!")
elif user_input==computer_choice:
  print("It's a draw")
elif user_input>computer_choice:
  print("You win!")
else:
    print("You Lost")
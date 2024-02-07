import random

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

#Write your code below this line 👇
options = [rock, paper, scissors]
print("What you chose, 0 rock, 1 paper or 2 scissors")
chosen = int(input())
print(options[chosen])

print("Computer choose:")
machine_choose = random.randint(0,2)
print(options[machine_choose])

if machine_choose == chosen:
    print("It's a draw")
elif chosen > 2 or chosen < 0:
    print("Invalide, you lose")
elif chosen == 0 and machine_choose == 2:
    print("You win!")
elif machine_choose == 0 and chosen == 2:
    print("You lose")
elif chosen > machine_choose:
    print("You win!")
elif chosen < machine_choose:
    print("You lose")

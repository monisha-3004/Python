import random

rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''

game_images = [rock, paper, scissors]
user_choise=int(input('''enter your user_choice
1.to play 
2.not to play\n'''))
player_score=0
comp_score=0


while user_choise==1:
    
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    if user_choice >= 3 or user_choice < 0: 
      print("You typed an invalid number, you lose!") 
    elif user_choice == 0 and computer_choice == 2:
      print("You win!")
      player_score+=1
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
      comp_score+=1
    elif computer_choice > user_choice:
      print("You lose")
      comp_score+=1
    elif user_choice > computer_choice:
      print("You win!")
      player_score+=1
    elif computer_choice == user_choice:
      print("It's a draw")
    user_choise=int(input('''enter your user_choice
                                1.to play 
                                2.not to play\n'''))
                                
print("GRAND TOTAL:\n")
print("player score:",player_score,"\n")
print("computer score:",comp_score,"\n")
                        
if player_score>comp_score:
    print("PLAYER WINS THE GAME!")
else:
    print("COMPUTER WINS THE GAME!")

import random

while True:
  
    user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")
    possible_options = ['R', 'P', 'S'] # list created
    pc_input = random.choice(possible_options)

    if(user_input == pc_input):
      if user_input == 'R':
       print("Player(Rock): CPU(Rock)") 
       print(f"\n It's a Tie, Both players chose Rock")
      elif user_input == 'P':
        print("Player(Paper): CPU(Paper)")
        print(f"\n It's a Tie, Both players chose Paper")
      elif user_input == 'S':
        print("Player(Scissors): CPU(Scissors)")
        print(f"\n It's a Tie, Both players chose Scissors")
         
      ans  = input("Do you wan to Play again? YES(Y) or NO(N): ")    

      if ans == 'n' or ans == 'N' or ans != 'Y':
        break

    elif user_input == 'R':
      if(pc_input == 'S'):
        print(f'\nPlayer(Rock): CPU(Scissors)')
        print("Rock beats Scissors, You win")
        break
      else:
        print(f'\nPlayer(Rock): CPU(Paper)')
        print("Paper beats rock, CPU wins")
        break

    elif user_input == 'P':
      if(pc_input == 'R'):
        print(f'\nPlayer(Paper): CPU(Rock)')
        print("Paper beats Rock, You win")
        break
      else:
        print(f'\nPlayer(Paper): CPU(Scissors)')
        print("Scissors beats paper, CPU wins")
        break  

    elif user_input == 'S':
      if(pc_input == 'P'):
        print(f'\nPlayer(Scissors): CPU(Paper)')
        print("Scissors beats Paper, You win")
        break
      else:
        print(f'\nPlayer(Scissors): CPU(Rock)')
        print("Rock beats Scissors, CPU wins")    
        break
    else:
      print("Error in chosen option")
      
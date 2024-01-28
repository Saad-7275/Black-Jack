import random

def get_choices():
  player_choice = input('Enter a choice: (rock, paper, scissors):')
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"Your Choice: {player}, computer choice: {computer}")
  if player == computer:
    return "Its a Tie!!"
  elif player == "rock":
    if computer == "paper":
      return "Paper Covers the Rock, You Lose."
    else:
      return "Rock Crushes Scissors, You Win!!"
  elif player == "paper":
    if computer == "scissors":
      return "Scissors Cuts Paper, You Lose."
    else:
      return "Paper Covers the Rock, You Win!!"
  elif player == "scissors":
    if computer == "rock":
      return "Rock Crushes Scissors, You Lose."
    else:
      return "Scissors Cuts Paper, You Win!!"


choice = get_choices()
result = check_win(choice["player"], choice["computer"])
print(result)
      
  
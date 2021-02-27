import art
import random
def deal_cards():
    """Returns a random card from the deck."""
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score,computer_score):
  """Compares user and computer score"""
  if user_score>21 and computer_score>21 :
    return "You lose. You went over."
  if user_score==computer_score:
    return "Draw"
  elif user_score==0:
    return "You win with blackjack"
  elif computer_score==0:
    return "You lose.computer win with blackjack"
  elif user_score>21:
    return "You lose. You went over."
  elif computer_score>21:
    return "you win. Computer went over."
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"

def play():
  """Starts game"""
  user_cards = []
  computer_cards = []
  game_ended=False
  for i in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  user_sum=calculate_score(user_cards)
  computer_sum=calculate_score(computer_cards)

  while not game_ended:
    print(f"Your cards: {user_cards}, current score: {user_sum}")
    print(f"Computer's First card: {computer_cards[0]}")
    if user_sum==0 or computer_cards==0 or user_sum>21:
      game_ended=True
    else:
      pickCard=input("Do you want to pick card: ")
      if pickCard=="y":
        user_cards.append(deal_cards())
        user_sum=calculate_score(user_cards)
      else:
        game_ended=True
  while computer_sum!=0 and computer_sum<17:
    computer_cards.append(deal_cards())
    computer_sum=calculate_score(computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_sum}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_sum}")
  print(compare(user_sum, computer_sum))

if __name__ == '__main__':
    print(art.logo)
    play()







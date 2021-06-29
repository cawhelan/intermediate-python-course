import random

def main():

  dice_rolls = 3
  dice_size = 6

  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    if roll == 4:
      print(f'You rolled a {roll}! Person to your left drinks')
    elif roll == 5:
      print(f'You rolled a {roll}! You drink')
    elif roll == 6:
      print(f'You rolled a {roll}! Person to your right drinks')
    else:
      print(f'You rolled a {roll}! Lucky, no one drinks')

if __name__== "__main__":
  main()